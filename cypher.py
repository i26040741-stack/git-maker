def ceasar(text,shift,encrypt = True):
    alphabets ="abcdefghijklmnopqrstuvwxyz"


    if not isinstance(shift,int):
        return "Enter only valid numeric number"

    if 1 >shift > 26:
        return "Pick numbers between 1 -26"

    if not encrypt:
        shift = - shift

    new = alphabets[shift:] + alphabets[:shift]
    matching_table = str.maketrans(alphabets+ alphabets.upper()
                                   , new + new.upper())
    activate = text.translate(matching_table)
    return activate

text = input("Enter the number ")
shift = int(input("How many different position do u want to move: "))

encrypt = ceasar(text,shift)
dencrypt = ceasar(text,shift,encrypt = False)

print(f"encrypt: {encrypt}")
print(f"dencrypt: {dencrypt}")





