import random
choices = ["rock", "paper", "scissors"]
while True:
    human_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
    computer_choice = random.choice(choices)
    if human_choice not in choices and human_choice != "quit":
        print("Invalid choice. Please try again.")
        continue
    elif human_choice == computer_choice:
        print(f"Both chose {human_choice}. It's a tie!")
    elif (human_choice == "rock" and computer_choice == "scissors") or \
         (human_choice == "paper" and computer_choice == "rock") or \
         (human_choice == "scissors" and computer_choice == "paper"):
        print(f"\nYou chose {human_choice}, computer chose {computer_choice}. You win!")
    elif human_choice == "quit":
        print("Thanks for playing!")
        break
    else:
        print(f"You chose {human_choice}, computer chose {computer_choice}. Computer wins!")