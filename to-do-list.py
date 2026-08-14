import json
tasks = []

def save_tasks():
      with open("tasks.json","w") as files:
            json.dump(tasks,files)
def load_tasks():
      global tasks
      try:
            with open("tasks.json","r") as files:
                  tasks = json.load(files)
      except FileNotFoundError:
            tasks = []
def menu():
    print("=" * 25)
    print("1) Add the task")
    print("2) Review the task")
    print("3) Remove the task")
    print("4) mark the task")
    print("5) Quit")
    print("=" * 25)

load_tasks()
while True:
        menu()
        try: 
            answer = int(input("Any task today: "))
        except ValueError:
              print("only number input: ")
              continue

        if answer == 1:
              choice = input("Write into the tasks: ")
              tasks.append({"name": choice,
                            "done": False
                            })
              save_tasks()
        elif answer == 2:
              for number,item in enumerate(tasks,start =1):
                    if item["done"]:
                          status = "[X]"
                    else:
                          status = "[ ]"
                    print(f"\n{status}|{number}: {item["name"]}")
        elif answer == 3:
              if not tasks:
                    print("NO task found!!")
                    continue
              for number,item in enumerate(tasks,start=1):
                    print(f"{number}: {item["name"]}")
              try:
                    choice = int(input("Enter the number to remove: "))
              except ValueError:
                    print("Only number valid: ")
                    continue
              if  1 <= choice <= len(tasks):
                    removed = tasks.pop(choice -1)
                    save_tasks()
                    print(f"removed: {removed["name"]}")
              else:
                    print("Out of the number")
        elif answer == 4:
              for number,item in enumerate(tasks,start=1):
                print(f"{number}: {item["name"]}")
              try:
                  choice = int(input("How many tasks have u finished?: "))
              except ValueError:
                    print("Only number: ")
                    continue
              for number,item in enumerate(tasks,start=1):
                    print(f"{number}: {item["name"]}")
              if 1 <= choice <= len(tasks):
                    tasks[choice-1]["done"] = True
                    save_tasks()
                    print(f"Completed: {tasks[choice-1]["name"]}")
              else:
                    print("Out of range")
        elif answer == 5:
              print("bye!!")
              break
        else:
              print("invalid enter")
              
              




