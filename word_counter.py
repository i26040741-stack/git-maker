while True:
    sentence = input("Type a sentence, or 'q' to quit: ").strip()

    if sentence.lower() == "q":
        print("Bye!")
        break

    if sentence == "":
        print("Please enter a sentence.")
        continue

    words = sentence.split()

    print(f"Sentence: {sentence}")
    print(f"Characters: {len(sentence)}")
    print(f"Words: {len(words)}")
    print()