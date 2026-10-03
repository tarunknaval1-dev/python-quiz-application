import json
import random
from datetime import datetime
from pathlib import Path

SCORES_FILE = Path("scores.json")

questions = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. func", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which symbol is used for a comment in Python?",
            "options": ["A. //", "B. #", "C. <!-- -->", "D. /* */"],
            "answer": "B"
        },
        {
            "question": "Which of these is a Python data type?",
            "options": ["A. list", "B. table", "C. folder", "D. webpage"],
            "answer": "A"
        }
    ],
    "Science": [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
            "answer": "B"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        }
    ],
    "General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["A. 365", "B. 364", "C. 366", "D. 367"],
            "answer": "C"
        },
        {
            "question": "Which is the largest ocean in the world?",
            "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        }
    ]
}


def load_scores():
    if SCORES_FILE.exists():
        with open(SCORES_FILE, "r") as file:
            return json.load(file)

    return []


def save_scores(scores):
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file, indent=4)


def save_quiz_result(name, category, difficulty, score, total_questions):
    scores = load_scores()
    percentage = (score / total_questions) * 100

    result = {
        "name": name,
        "category": category,
        "difficulty": difficulty,
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    scores.append(result)
    save_scores(scores)


def show_high_scores():
    scores = load_scores()

    if not scores:
        print("\nNo quiz scores saved yet.\n")
        return

    scores.sort(key=lambda item: item["percentage"], reverse=True)

    print("\n--- High Score Leaderboard ---")

    for number, score in enumerate(scores[:5], start=1):
        print(
            f"{number}. {score['name']} | "
            f"{score['category']} | "
            f"{score['difficulty']} | "
            f"{score['score']}/{score['total_questions']} | "
            f"{score['percentage']:.0f}% | "
            f"{score['date']}"
        )

    print()


def choose_category():
    category_names = list(questions.keys())

    print("\n--- Quiz Categories ---")

    for number, category in enumerate(category_names, start=1):
        print(f"{number}. {category}")

    while True:
        try:
            choice = int(input("Choose a category: "))

            if 1 <= choice <= len(category_names):
                return category_names[choice - 1]

            print("Please choose a valid category number.")

        except ValueError:
            print("Please enter a number.")


def choose_difficulty():
    difficulties = {
        "1": {"name": "Easy", "question_count": 1},
        "2": {"name": "Medium", "question_count": 2},
        "3": {"name": "Hard", "question_count": 3}
    }

    print("\n--- Difficulty Level ---")
    print("1. Easy - 1 question")
    print("2. Medium - 2 questions")
    print("3. Hard - 3 questions")

    while True:
        choice = input("Choose difficulty: ").strip()

        if choice in difficulties:
            return difficulties[choice]

        print("Please choose 1, 2, or 3.")


def get_performance_message(percentage):
    if percentage == 100:
        return "Excellent! Perfect score!"
    elif percentage >= 70:
        return "Great job! You have strong knowledge."
    elif percentage >= 50:
        return "Good effort! Keep practicing."
    else:
        return "Keep learning and try again."


def show_review(answers):
    print("\n--- Answer Review ---")

    for number, item in enumerate(answers, start=1):
        print(f"\nQuestion {number}: {item['question']}")
        print(f"Your answer: {item['user_answer']}")
        print(f"Correct answer: {item['correct_answer']}")

        if item["is_correct"]:
            print("Result: Correct")
        else:
            print("Result: Wrong")


def start_quiz(name):
    category = choose_category()
    difficulty = choose_difficulty()
    score = 0
    answers = []

    selected_questions = random.sample(
        questions[category],
        difficulty["question_count"]
    )

    print(f"\n--- {category} Quiz ({difficulty['name']}) ---")
    print("Questions are selected randomly.")
    print("Choose the correct option: A, B, C, or D.\n")

    for number, quiz in enumerate(selected_questions, start=1):
        print(f"Question {number}/{len(selected_questions)}: {quiz['question']}")

        for option in quiz["options"]:
            print(option)

        user_answer = input("Your answer: ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid choice. Please enter A, B, C, or D.")
            user_answer = input("Your answer: ").strip().upper()

        is_correct = user_answer == quiz["answer"]

        answers.append({
            "question": quiz["question"],
            "user_answer": user_answer,
            "correct_answer": quiz["answer"],
            "is_correct": is_correct
        })

        if is_correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz['answer']}.\n")

    percentage = (score / len(selected_questions)) * 100

    print("--- Quiz Completed ---")
    print(f"Category: {category}")
    print(f"Difficulty: {difficulty['name']}")
    print(f"Your score: {score}/{len(selected_questions)}")
    print(f"Percentage: {percentage:.0f}%")
    print(get_performance_message(percentage))

    save_quiz_result(
        name,
        category,
        difficulty["name"],
        score,
        len(selected_questions)
    )

    print("Your result has been saved to the leaderboard.")
    show_review(answers)


def main():
    print("Welcome to the Python Quiz Application!")

    name = input("Enter your name: ").strip()

    if not name:
        name = "Player"

    while True:
        print("\n--- Main Menu ---")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_quiz(name)
        elif choice == "2":
            show_high_scores()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()