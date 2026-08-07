def show_menu():
    print("╔══════════════════════════════════════╗")
    print("║      METRIC CONVERSION CHALLENGE     ║")
    print("║   Who Wants to Be a Millionaire?     ║")
    print("╠══════════════════════════════════════╣")
    print("║  A. Kilometres → Miles               ║")
    print("║  B. Miles → Kilometres               ║")
    print("║  C. Kilograms → Pounds               ║")
    print("║  D. Celsius → Fahrenheit             ║")
    print("║  Q. Quit                             ║")
    print("╚══════════════════════════════════════╝")


def get_question(choice):
    if choice == "A":
        return (
            "How many miles are in 10 kilometres?",
            ["A. 6.21", "B. 8.05", "C. 12.43", "D. 16.09"],
            "A",
        )
    if choice == "B":
        return (
            "How many kilometres are in 5 miles?",
            ["A. 3.11", "B. 8.05", "C. 10.00", "D. 12.43"],
            "B",
        )
    if choice == "C":
        return (
            "How many pounds are in 3 kilograms?",
            ["A. 4.41", "B. 5.51", "C. 6.61", "D. 7.71"],
            "C",
        )
    if choice == "D":
        return (
            "What is 25°C in Fahrenheit?",
            ["A. 45°F", "B. 57°F", "C. 68°F", "D. 77°F"],
            "D",
        )
    raise ValueError("Invalid choice")


def main():
    score = 0

    while True:
        show_menu()
        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            print(f"Thanks for playing! Final score: {score}")
            break

        if choice not in {"A", "B", "C", "D"}:
            print("Invalid choice. Please try again.\n")
            continue

        question, options, correct_answer = get_question(choice)
        print(f"\n{question}")
        for option in options:
            print(option)

        answer = input("Choose A, B, C, or D: ").strip().upper()

        if answer == correct_answer:
            score += 1000
            print("Correct! Well done.\n")
        else:
            print("Wrong answer! Game over.\n")
            print(f"Final score: {score}")
            break


if __name__ == "__main__":
    main()

