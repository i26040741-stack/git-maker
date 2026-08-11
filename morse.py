morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}





def encoded(choice):
    finals = ""
    for item in choice:
        result = morse[item]
        finals += result + " "
    return finals

def dencoded(choice):
    reversed_code = {}
    for letter,code in morse.items():
        reversed_code[code] = letter

    changed = ""
    for item in choice.split():
        changed += reversed_code[item]
    return changed


def menu():
    print("=" * 12)
    print("1) encode")
    print("2) decode")
    print("3) exit")
    print("=" * 12)



while True:
    menu()
    try:
        answer = int(input("Encode or Decode: "))
    except ValueError:
        print("Enter only number: ")   
    choice = input("Enter your encoded words or decoded words: ")
    if answer == 1:
        encode = encoded(choice)
        print(f" Enter words to encode:{encode}")
    elif answer == 2:
        decode = dencoded(choice)
        print(f"The decoded result:{decode}")

    elif answer == 3:
        print("BYE!")
        break
    else:
        print("Choose the options again?")
        continue




