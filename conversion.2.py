import math

def show_menu():
    print("╔══════════════════════════════════════╗")
    print("║          📐 AREA CALCULATOR          ║")
    print("╠══════════════════════════════════════╣")
    print("║  A. Rectangle                        ║")
    print("║  B. Triangle                         ║")
    print("║  C. Circle                           ║")
    print("║  Q. Quit                             ║")
    print("╚══════════════════════════════════════╝")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Enter only valid number")

def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius ** 2


def main():
    while True:
        show_menu()
        choice = input("Choose the options: ").lower().strip()
        if choice not in ["a","b","c","q"]:
            print("Please pick one of these options here: ")
            continue

        if choice == "q":
            print("bye!")
            break

        if choice == "a":
            length = get_number("Enter the length: ")
            width = get_number("Enter the width: ")
            area = rectangle_area(length, width)
            print(f"Rectangle area = {area:.2f}")

        elif choice == "b":
            base = get_number("Enter the base: ")
            height = get_number("Enter the height: ")
            area = triangle_area(base, height)
            print(f"Triangle area = {area:.2f}")

        elif choice == "c":
            radius = get_number("Enter the radius: ")
            area = circle_area(radius)
            print(f"Circle area = {area:.2f} ")

        print()



main()


