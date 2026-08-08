import random 
secrate_number = random.randint(1,100)
attempt = 0
while True:
    try:
        guess = int(input("guess: "))
    except ValueError:
        print("Enter the number!!")
        continue
    if guess < 1 or guess > 100:
        print("within 100")
        continue

    attempt += 1

    if guess < secrate_number:
        print("too low!")
    elif guess > secrate_number:
        print("too high!")
    else:
        print("correct!")
        print(f"attempt: {attempt}")
        break
