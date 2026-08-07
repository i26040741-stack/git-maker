
 

def show_menu():
    print("╔══════════════════════════════════════╗")
    print("║     METRIC CONVERSION CHALLENGE      ║")
    print("║                                      ║")
    print("╠══════════════════════════════════════╣")
    print("║  A. Kilometres → Miles               ║")
    print("║  B. Miles → Kilometres               ║")
    print("║  C. Kilograms → Pounds               ║")
    print("║  D. Pounds → Kilograms               ║")
    print("║  E. Celsius → Fahrenheit             ║")
    print("║  F. Fahrenheit → Celsius             ║")
    print("║  Q. Quit                             ║")
    print("╚══════════════════════════════════════╝")


def kilometres_to_miles(kilometres):
    return kilometres * 0.621371


def miles_to_kilometres(miles):
    return miles * 1.60934


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    return pounds * 0.453592


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


while True:
    show_menu()
    try:
        answer = input("Choose an option: ").lower().strip()
        if answer not in ["a", "b", "c", "d", "e", "f", "q"]:
            raise ValueError

    except ValueError:
        print("Choose only fromt those a,b,c... :")
        continue


    if answer == "q":
        print("BYE!!")
        break

    while True:
        try:
            value = float(input("Enter the value that u want converted: "))
            break
            
        except ValueError:
            print("enter valid numeric number!")

    if answer == "a":
        miles = kilometres_to_miles(value)
        print(f"{value} km = {miles:.2f} miles")

    elif answer == "b":
        kilometres = miles_to_kilometres(value)
        print(f"{value} miles = {kilometres:.2f} km")

    elif answer == "c":
        pounds = kilograms_to_pounds(value)
        print(f"{value} kg = {pounds:.2f} pounds")

    elif answer == "d":
        kilograms = pounds_to_kilograms(value)
        print(f"{value} pounds = {kilograms:.2f} kg")

    elif answer == "e":
        fahrenheit = celsius_to_fahrenheit(value)
        print(f"{value}°C = {fahrenheit:.2f}°F")

    elif answer == "f":
        celsius = fahrenheit_to_celsius(value)
        print(f"{value}°F = {celsius:.2f}°C")

    print()
