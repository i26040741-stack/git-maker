import random
fortunes = ["1. Today is a great day to start something new.",
"2. A surprise opportunity is coming your way.",
"3. Your patience will be rewarded soon.",
"4. Someone important will appreciate your hard work.",
"5. Believe in yourself, and success will follow."]
cokie = input("Do you want a fortune cookie? (yes/no): ")
if cokie.lower() == 'yes':
    print(random.choice(fortunes))
else:
    print("Maybe next time!")