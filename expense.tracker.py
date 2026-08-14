import json
expenses = []

def save_load():
   with open("expense.json","w")as files:
       json.dump(expenses,files)

def load_load():
   global expenses
   try:
      with open('expense.json','r') as files:
         expenses = json.load(files)
   except FileNotFoundError:
      expenses = []

load_load()
def menu():
    print("=" * 25)
    print("1) Add Expense")
    print("2) View Expenses")
    print("3) Remove Expense")
    print("4) Exit")
    print("=" * 25)

while True:
   menu()
   try:
      answer = int(input("Choose the option: "))
   except ValueError:
      print("Only choose the options")
      continue
   if answer == 1:
      choice = input("the name of expense: ")
      amount = float(input("amount: "))
      category = input("Category: ")
      expenses.append({"name": choice,
                       "amount": amount,
                       "category": category
      })
      save_load()

   elif answer == 2:
      if not expenses:
         print("No expenses yet")
         continue
      total = 0
      for number,item in enumerate(expenses,start=1):
         print(f{number}:{item["name"]}")
         print(f"amount:{item["amount"]:.2f}")
         print(f"category: {item["category"]}")
         total += item["amount"]
      print("-" * 25)
      print(f"Total spending: {total}")
         
   elif answer == 3:
      for number,item in enumerate(expenses,start=1):
         print(f"{number}:{item}")
      try:
         choice = int(input("write to remove: "))
      except ValueError:
         print("Invalid enter!!")
         continue
      if 1<= choice <= len(expenses):
         removed = expenses.pop(choice-1)
         save_load()
         print("You removed:",removed)
      else:
         print("out of the range")
         continue
   elif answer == 4:
      print("BYE!")
      break
   else:
      print("valid enter")
 
