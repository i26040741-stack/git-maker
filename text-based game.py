print("⚔️ ESCAPE THE HAUNTED CASTLE ⚔️")
print("You wake up inside a dark castle room.")
print("You see a wooden door and a mysterious chest.")

choice = input("Choose 'door' or 'chest': ").lower().strip()
while True:  
   choice = input("Choose only 'door' or 'chest': ").lower().strip()
   if choice in ["door", "chest"]:
       break

if choice == "door":
    print("You open the door and find a long corridor.")
    print("At the end of the corridor, you see a staircase leading down.")
    choice = input("Do you want to go 'down' the stairs or 'explore' the corridor? ").lower().strip()
    if choice == "down":
        print("the stairs that you descend collpase and you fall into a pit of spikes. You have met your demise.")
        print("GAME OVER")
    elif choice == "explore":
        print("You explore the corridor and find a hidden passage leading to a secret room.")
        print("Inside the room, you find a map: it shows the way to escape the castle!")
        print("You follow the map and successfully escape the haunted castle!")
        print("CONGRATULATIONS! YOU HAVE ESCAPED THE HAUNTED CASTLE!")
    else:
        print("Invalid choice. You hesitate and a ghost appears, scaring you to death.")
        print("GAME OVER")
elif choice == "chest":
    print("You open the chest and find a drink and a note.")
    choice = input("Do you want to 'drink' the drink or 'read' the note? ").lower().strip()
    if choice == "drink":
        print("You drink the mysterious liquid and feel dizzy and poisoned.")
        print("You collapse to the ground and meet your demise.")
        print("GAME OVER")
    elif choice == "read":
        print("You read the note and it says: 'The key to escape is hidden in the library.'")
        print("You find a secret passage leading to the library.")
        print("In the library, you find a key hidden behind a book.")
        print("You use the key to unlock a door that leads you outside the castle!")
        print("CONGRATULATIONS! YOU HAVE ESCAPED THE HAUNTED CASTLE!")
    else:
        print("Invalid choice. You hesitate and a ghost appears, scaring you to death.")
        print("GAME OVER")
else:
    print("Invalid choice. Make sure to choose either 'door' or 'chest'.")
    print("GAME OVER")