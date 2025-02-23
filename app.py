import os
import json
import base64
import sys
import re
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.newsrep.crew import Newsrep

# Load environment variables
load_dotenv()

# Ensure Python can find the newsrep module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Firebase Initialization
firebase_key_base64 = os.getenv("FIREBASE_KEY_BASE64")

if firebase_key_base64:
    try:
        firebase_key_json = json.loads(base64.b64decode(firebase_key_base64).decode("utf-8"))
        cred = credentials.Certificate(firebase_key_json)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("Connected to Firestore successfully")
    except Exception as e:
        print(f"Error initializing Firestore: {e}")
else:
    print("FIREBASE_KEY_BASE64 not found in environment variables")

# Pydantic model for user input
class NewsRequest(BaseModel):
    topic: str

def generate_slug(title):
    """Convert title into a URL-friendly slug"""
    return re.sub(r'\W+', '-', title.lower()).strip('-')

def save_to_firestore(topic, result):
    """Extracts title & content from CrewAI output and saves to Firestore."""
    try:
        result_dict = result.__dict__

        last_task = None
        for task in result_dict.get("tasks_output", []):
            if task.name == "news_writing_task":
                last_task = task

        if last_task:
            full_text = last_task.raw.strip()
            title = full_text.split("\n")[0].replace("# ", "").strip()
            content = full_text
            slug = generate_slug(title)  # Generate slug from title
        else:
            title = "No Title Found"
            content = "No Content Found"
            slug = "no-title"

        news_doc = {
            "topic": topic,
            "title": title,
            "slug": slug,
            "content": content,
            "created_at": firestore.SERVER_TIMESTAMP
        }

        db.collection("news_articles").add(news_doc)
        print(f"News report saved to Firestore with slug: {slug}")

    except Exception as e:
        print(f"Error saving to Firestore: {e}")

@app.post("/generate_news/")
async def generate_news(request: NewsRequest, background_tasks: BackgroundTasks):
    """Handles news generation asynchronously and saves to Firestore"""
    try:
        newsrep = Newsrep()
        result = newsrep.crew().kickoff(inputs={"topic": request.topic})

        # Save to Firestore in the background
        background_tasks.add_task(save_to_firestore, request.topic, result)

        return {"message": "Processing in background, check Firestore later"}
    except Exception as e:
        return {"error": f"Error processing news: {e}"}

@app.get("/news/")
async def get_news():
    """Retrieve latest news reports from Firestore"""
    try:
        news_ref = db.collection("news_articles").order_by("created_at", direction=firestore.Query.DESCENDING).limit(10)
        news = news_ref.stream()

        news_list = [
            {
                "topic": doc.to_dict().get("topic", "Unknown Topic"),
                "title": doc.to_dict().get("title", "No Title"),
                "slug": doc.to_dict().get("slug", "no-title"),
                "content": doc.to_dict().get("content", "No Content"),
            }
            for doc in news
        ]
        return news_list
    except Exception as e:
        return {"error": f"Error fetching news: {e}"}
