"""
DDCO Quiz Game
--------------
A simple command-line quiz on Digital Design & Computer Organization.
The user answers 5 multiple-choice questions (A, B, C, or D)
and gets a final score out of 5.

Run with:  python ddco_quiz.py
"""

# Each question is a dictionary with three keys:
#   "question" -> the question text
#   "options"  -> a dictionary mapping letters (A-D) to answer text
#   "answer"   -> the letter of the correct option
QUESTIONS = [
    {
        "question": "How many select lines does an 8:1 multiplexer need?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "8"},
        "answer": "B",
    },
    {
        "question": "Which logic gate is called a 'universal gate'?",
        "options": {"A": "AND", "B": "OR", "C": "NAND", "D": "XOR"},
        "answer": "C",
    },
    {
        "question": "The SUM output of a half adder is equivalent to which gate?",
        "options": {"A": "AND", "B": "XOR", "C": "OR", "D": "NOR"},
        "answer": "B",
    },
    {
        "question": "Which register holds the address of the next instruction to execute?",
        "options": {
            "A": "Program Counter (PC)",
            "B": "Accumulator",
            "C": "Stack Pointer",
            "D": "Instruction Register",
        },
        "answer": "A",
    },
    {
        "question": "Which is the fastest memory in the memory hierarchy?",
        "options": {"A": "Hard Disk", "B": "RAM", "C": "Cache", "D": "CPU Registers"},
        "answer": "D",
    },
]


def display_question(number, total, q):
    """
    Print one question and its options to the screen.

    number : the question number (starting from 1)
    total  : total number of questions in the quiz
    q      : the question dictionary from QUESTIONS
    """
    print(f"\nQuestion {number}/{total}: {q['question']}")
    for letter, text in q["options"].items():
        print(f"  {letter}) {text}")


def get_user_answer():
    """
    Ask the user for an answer and keep asking until they type
    a valid option (A, B, C, or D). Returns the answer in uppercase.
    """
    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in ("A", "B", "C", "D"):
            return choice
        print("Invalid input. Please enter A, B, C, or D.")


def check_answer(user_choice, q):
    """
    Compare the user's choice with the correct answer.
    Prints feedback and returns True if correct, otherwise False.
    """
    if user_choice == q["answer"]:
        print("Correct!")
        return True

    correct_letter = q["answer"]
    correct_text = q["options"][correct_letter]
    print(f"Wrong. The correct answer is {correct_letter}) {correct_text}")
    return False


def run_quiz():
    """
    Run the whole quiz: loop through every question, collect answers,
    keep track of the score, and return the final score.
    """
    score = 0
    total = len(QUESTIONS)

    for number, q in enumerate(QUESTIONS, start=1):
        display_question(number, total, q)
        user_choice = get_user_answer()
        if check_answer(user_choice, q):
            score += 1  # add a point for each correct answer

    return score


def show_result(score, total):
    """
    Print the final score along with a short message based on performance.
    """
    print("\n" + "=" * 30)
    print(f"Final Score: {score}/{total}")
    print("=" * 30)

    if score == total:
        print("Perfect! You really know your DDCO!")
    elif score >= 3:
        print("Good job! A little more revision and you'll ace it.")
    else:
        print("Keep practicing - review the basics and try again!")


def main():
    """
    Entry point: show a welcome message, run the quiz,
    and display the result.
    """
    print("=== Welcome to the DDCO Quiz! ===")
    print("Answer each question by typing A, B, C, or D.")

    score = run_quiz()
    show_result(score, len(QUESTIONS))


# This ensures main() only runs when the file is executed directly,
# not when it is imported as a module in another program.
if __name__ == "__main__":
    main()
