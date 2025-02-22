#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from newsrep.crew import Newsrep

# Suppress unnecessary warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def get_user_topic():
    """
    Get the topic dynamically from the user.
    - If provided via CLI, use that.
    - Otherwise, prompt for manual input.
    """
    if len(sys.argv) > 2:  # If topic is provided via CLI arguments
        return " ".join(sys.argv[2:])
    else:  # Otherwise, ask the user manually
        return input("Enter the topic you want to research: ").strip()


def run():
    """
    Runs the NewsRep AI-powered system dynamically with a user-defined topic.
    Usage:
        python main.py run "Impact of AI on Finance"
    """
    topic = get_user_topic()
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        print(f"\n Running NewsRep Crew on Topic: {topic}")
        newsrep = Newsrep()
        newsrep.crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Error while running: {e}")


def train():
    """
    Trains the AI Crew with a given number of iterations.
    Usage:
        python main.py train <num_iterations> <output_filename> "Topic"
    """
    topic = get_user_topic()
    if len(sys.argv) < 4:
        print(" Error: Missing arguments. Usage: python main.py train <num_iterations> <output_filename> \"Topic\"")
        return

    try:
        num_iterations = int(sys.argv[2])
        filename = sys.argv[3]
        inputs = {'topic': topic}

        print(f"\n🎓 Training AI Crew on Topic: {topic} | Iterations: {num_iterations}")
        Newsrep().crew().train(n_iterations=num_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        print(f" Error while training: {e}")


def replay():
    """
    Replays a previous execution from a specific task.
    Usage:
        python main.py replay <task_id>
    """
    if len(sys.argv) < 3:
        print(" Error: Missing task_id. Usage: python main.py replay <task_id>")
        return

    try:
        task_id = sys.argv[2]
        print(f"\n Replaying Task ID: {task_id}")
        Newsrep().crew().replay(task_id=task_id)
    except Exception as e:
        print(f" Error while replaying: {e}")


def test():
    """
    Tests the AI Crew execution with OpenAI model.
    Usage:
        python main.py test <num_iterations> <openai_model_name> "Topic"
    """
    topic = get_user_topic()
    if len(sys.argv) < 4:
        print(" Error: Missing arguments. Usage: python main.py test <num_iterations> <openai_model_name> \"Topic\"")
        return

    try:
        num_iterations = int(sys.argv[2])
        model_name = sys.argv[3]
        inputs = {'topic': topic}

        print(f"\n Testing AI Crew on Topic: {topic} | Model: {model_name} | Iterations: {num_iterations}")
        Newsrep().crew().test(n_iterations=num_iterations, openai_model_name=model_name, inputs=inputs)
    except Exception as e:
        print(f" Error while testing: {e}")


def main():
    """
    Main function to handle command-line execution.
    """
    if len(sys.argv) < 2:
        print(" Error: Missing command. Usage: python main.py <run|train|replay|test> <args>")
        return

    command = sys.argv[1].lower()

    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(" Error: Unknown command. Usage: python main.py <run|train|replay|test> <args>")


if __name__ == "__main__":
    main()
