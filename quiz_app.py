questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used to build this quiz application?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Unit",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. /* */"],
        "answer": "B"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. list", "B. table", "C. filebox", "D. folder"],
        "answer": "A"
    }
]


def start_quiz():
    score = 0

    print("\nWelcome to the Python Quiz Application!")
    print("Choose the correct option: A, B, C, or D.\n")

    for number, quiz in enumerate(questions, start=1):
        print(f"Question {number}: {quiz['question']}")

        for option in quiz["options"]:
            print(option)

        user_answer = input("Your answer: ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid choice. Please enter A, B, C, or D.")
            user_answer = input("Your answer: ").strip().upper()

        if user_answer == quiz["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz['answer']}.\n")

    print("--- Quiz Completed ---")
    print(f"Your score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.0f}%")


if __name__ == "__main__":
    start_quiz()