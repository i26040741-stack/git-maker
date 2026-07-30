import random


def roll_dice():
    return random.randint(1, 6)


print("Welcome to the Dice Simulator!")

while True:
    answer = input("Do you want to roll the dice? (yes/no): ").lower()

    if answer == "yes":
        dice_rolls = []

        for _ in range(3):
            dice_rolls.append(roll_dice())

        for number, value in enumerate(dice_rolls, start=1):
            print(f"Die {number}: {value}")

        total = sum(dice_rolls)
        print(f"Total of the three dice: {total}")

    elif answer == "no":
        print("Thanks for playing!")
        break

    else:
        print("Please enter yes or no.")