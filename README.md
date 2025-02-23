# AI News Agent - Next.js, FastAPI, Firestore, CrewAI

## Overview

AI News Agent is a scalable AI-powered news reporting web application that enables users to generate and browse AI-curated news articles. This project utilizes:

- **Frontend:** Next.js (App Router with TypeScript)
- **Backend:** FastAPI (Python)
- **Database:** Firestore (Google Firebase)
- **AI Processing:** CrewAI Agents

---

## Features

- **Generate AI-powered news articles** using CrewAI
- **Search and browse existing news articles**
- **Firestore database integration** for storing and retrieving articles
- **Next.js frontend with Tailwind CSS & ShadCN components**
- **FastAPI backend for API communication**
- **Support for pagination & article slugs**

---

## Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/ManyamSanjayKumarReddy/fastapibackend-newsagent.git backend
cd backend
```

```bash
git clone https://github.com/ManyamSanjayKumarReddy/AI-News-Reporter-Frontend.git frontend-next
cd frontend-next
```

---

## **Backend Setup (FastAPI + Firestore)**

### **2. Create a Python Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**

```bash
pip install -r backend/requirements.txt
```

### **4. Setup Firestore Credentials**

- Place your Firebase credentials file (`firebase_key.json`) inside the `backend` folder.
- Update `backend/config.py` with your Firestore project details.

### **5. Run the Backend**

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will now be available at `http://127.0.0.1:8000`.

**Live Backend Server:** [FastAPI Backend](https://fastapibackend-newsagent.onrender.com/)

---

## **Frontend Setup (Next.js + Tailwind CSS + ShadCN)**

### **6. Install Dependencies**

```bash
cd frontend-next
npm install
```

### **7. Setup Environment Variables**

Create a `.env.local` file in `frontend-next` and add:

```bash
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
DATABASE_URL=<your_database_url>
MODEL=<your_model>
GEMINI_API_KEY=<your_gemini_api_key>
SERPER_API_KEY=<your_serper_api_key>
FIREBASE_KEY_BASE64=<your_firebase_key_base64>
```

### **8. Run the Frontend**

```bash
npm run dev
```

The frontend will now be available at `http://localhost:3000`.

**Live Frontend Server:** [AI News Agent Frontend](https://ai-news-reporter-frontend.vercel.app/)

---

## **Project Structure**

```
AI-News-Agent/
├── backend/
│   ├── app.py  # FastAPI main app
│   ├── crew.py  # CrewAI agents setup
│   ├── firestore.py  # Firestore DB connection
│   ├── requirements.txt  # Backend dependencies
│   └── config.py  # Configurations
│
├── frontend-next/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── pages/
│   ├── styles/
│   ├── tailwind.config.ts  # Tailwind CSS config
│   ├── .env.local  # API config
│   ├── next.config.js  # Next.js config
│   └── package.json  # Frontend dependencies
```

---

## **API Endpoints**

| Method   | Endpoint          | Description                |
| -------- | ----------------- | -------------------------- |
| **POST** | `/generate_news/` | Generate a news article    |
| **GET**  | `/news/`          | Fetch latest news articles |

---

## **CrewAI Agent Workflow**

### **Agents**

1. **Web Searcher:** Fetches latest news from sources
2. **News Optimizer:** Processes and refines news content
3. **News Writer:** Generates a structured AI-written news article

### **Tasks**

- **Search Task:** Uses `SerperDevTool` for web scraping
- **Optimize Task:** Uses `Gemini Flash 1.5` for summarization
- **Write Task:** Converts refined content into an engaging news article

---

## **Deployment**

### **Deploy Backend to Render/Vercel/AWS EC2**

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
```

### **Deploy Frontend to Vercel**

```bash
cd frontend-next
vercel deploy
```

---

## **Troubleshooting**

- **Database connection issues?** Ensure Firestore credentials are correctly set.
- **Next.js API fetch error?** Verify `NEXT_PUBLIC_API_URL` in `.env.local`.
- **FastAPI not running?** Check `uvicorn` logs for errors.

---

## **Contributing**

Feel free to submit PRs or issues to improve the project!

---

## **Author**

M Sanjay Kumar Reddy

