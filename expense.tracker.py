

expenses = []
total = 0
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

   elif answer == 2:
      if not expenses:
         print("No expenses yet")
         continue
      total += item["amount"]
      for number,item in enumerate(expenses,start=1):
         print(f"\n{number}:{item["name"]}"
              f"amount: {item["amount"]:.2f}"
              f"category: {item["category"]}")
         print(f"total expenses:RM{total}")
         
   elif answer == 3:
      for number,item in enumerate(expenses,start=1):
         print(f"{number}:{item}")
      try:
         choice = int(input("write to remove: "))
      except ValueError:
         print("Invalid enter!!")
         continue
      if 1<= choice <= len(expenses):
         removed = expenses.pop(expenses[choice-1])
         print("You removed:",removed)
      else:
         print("out of the range")
         continue
   elif answer == 4:
      print("BYE!")
      break
   else:
      print("valid enter")
 