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


def start_quiz(category):
    score = 0
    selected_questions = questions[category]

    print(f"\n--- {category} Quiz ---")
    print("Choose the correct option: A, B, C, or D.\n")

    for number, quiz in enumerate(selected_questions, start=1):
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

    percentage = (score / len(selected_questions)) * 100

    print("--- Quiz Completed ---")
    print(f"Category: {category}")
    print(f"Your score: {score}/{len(selected_questions)}")
    print(f"Percentage: {percentage:.0f}%")


def main():
    print("Welcome to the Python Quiz Application!")

    while True:
        category = choose_category()
        start_quiz(category)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()