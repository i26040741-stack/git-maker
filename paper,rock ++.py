import random
choices = ["rock", "paper", "scissors","lizard","spock"]
beat  = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}
while True:
    human_choice = input("Enter rock, paper, scissors, lizard, or spock (or 'quit' to exit): ").lower().strip()
    computer_choice = random.choice(choices)
    if human_choice not in choices and human_choice != "quit":
        print("Invalid choice. Please try again.")
        continue
    elif human_choice == computer_choice:
        print(f"Both chose {human_choice}. It's a tie!")
    elif computer_choice in beat[human_choice]:
        print(f"\nYou chose {human_choice}, computer chose {computer_choice}. You win!")
    elif human_choice == "quit":
        print("Thanks for playing!")
        break
    else:
        print(f"You chose {human_choice}, computer chose {computer_choice}. Computer wins!")