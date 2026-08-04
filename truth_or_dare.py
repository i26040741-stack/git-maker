import random
truth = {
    "What is the worst habit you have?",
    "What is something you're afraid to tell your friends?",
    "What is the weirdest dream you've ever had?",
    "What is something you've lied about?",
    "What is the most embarrassing thing that has happened to you?"
}
dare = {
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Do 10 jumping jacks.",
    "Dance for 1 minute without music.",
    "Do an impression of your favorite celebrity."
}
user_choice = input("Choose 'truth' or 'dare or 'quit': ").strip().lower()
while True:
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    elif user_choice == "truth":
        question = random.choice(truth)
        print(f"Truth: {question}")
    elif user_choice == "dare":
        challenge = random.choice(dare)
        print(f"Dare: {challenge}")
    else:
        print("Invalid choice. Please choose 'truth', 'dare', or 'quit'.")
    user_choice = input("Choose 'truth' or 'dare or 'quit': ").strip().lower()


