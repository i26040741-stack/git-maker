import json
contact = []
def save_load():
    with open("contact.json","w") as files:     
      json.dump(contact,files)
 
def load_load():
    global contact
    try:
        with open("contact.json","r")as files:
            contact = json.load(files)
    except FileNotFoundError:
        contact = []
        
    

contact = []

def menu():
    print("=" * 25)
    print("1) Add Contact")
    print("2) View Contacts")
    print("3) Search Contact")
    print("4) Update Contact")
    print("5) Delete Contact")
    print("6) Exit")
    print("=" * 25)

load_load()
while True:
    menu()

    try:
        answer = int(input("Choose an option: "))
    except ValueError:
        print("Enter a number only.")
        continue

    if answer == 1:
        name = input("write name here: ")
        email = input("write email here: ")
        address = input("write address here: ")
        number = int(input("write number here: "))
        contact.append({"name": name,
                        "email": email,
                        "address": address,
                        "number": number
                        })
        save_load()

    elif answer == 2:
       for number,item in enumerate(contact,start=1):
           print(f"{number}: {item["name"]}")
           print(f"email - {item["email"]}")
           print(f"address - {item['address']}")
           print(f"number - {item['number']}")

    elif answer == 3:
        search = input("Search here: ")
        found = False
        for item in contact:
            if item["name"].lower() == search.lower():
                print(item)
                found = True
                break
        if not found:
          print("no contact found!")
            
    elif answer == 4:
        found = False
        search = input("Search here: ")
        for item in contact:
            if item["name"].lower() == search.lower():
                found = True
                print("1) Name")
                print("2) Email")
                print("3) Address")
                print("4) Phone")
                print("5) back!")
                choice = int(input("choose the option: "))
                if choice == 1:
                    update = input("update name: ")
                    item["name"] = update
                    found = True
                    save_load()
                    break
                elif choice == 2:
                    update = input("update email: ")
                    item["email"] = update
                    found = True
                    save_load()
                    break
                elif choice == 3:
                    update = input("update address: ")
                    item["address"] = update
                    found = True
                    save_load()
                    break
                elif choice == 4:
                    update = int(input("update number: "))
                    item["number"] = update
                    found = True
                    save_load()
                    break
                else:
                    break
        if not found:
                print("Empty!!")
                    

    elif answer == 5:
        for number,item in enumerate(contact,start=1):
           print(f"{number}: {item["name"]}")
           print(f"email - {item["email"]}")
           print(f"address - {item['address']}")
           print(f"number - {item['number']}")
        choice = int(input("choose the number to delete: "))
        if 1<= choice <= len(contact):
               contact.pop(choice-1)
               save_load()
        else:
               print("Out of the range")
            

    elif answer == 6:
        print("Bye!")
        break

    else:
        print("Choose between 1 and 6.")
