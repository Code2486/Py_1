#Task Manager

import datetime

File_Name = "Task manager"

Works = []

try:
    file = open(File_Name, "r", encoding="utf-8")
    for line in file:
        title, done, date = line.strip().split("|")
        task = {"title": title, "done": done == "True", "date": date}
        Works.append(task)
    file.close()
except:
    pass

while True:
    print("\n*** MENU ***")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose: ")
    if choice == "1":
        task_title = input("Task title: ")
        task_date = datetime.date.today().isoformat()
        task = {"title": task_title, "done": False, "date": task_date}
        Works.append(task)

    elif choice == "2":
        if len(Works) == 0:
            print("No tasks found.")
        for i in range(len(Works)):
            status = "Done" if Works[i]["done"] else "Not Done"
            print(i + 1, "-", Works[i]["title"], "-", status, "-", Works[i]["date"])

    elif choice == "3":
        task_num = int(input("Task number to mark as done: ")) - 1
        if 0 <= task_num < len(Works):
            Works[task_num]["done"] = True

    elif choice == "4":
        task_num = int(input("Task number to delete: ")) - 1
        if 0 <= task_num < len(Works):
            Works.pop(task_num)

    elif choice == "5":
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice!")

    file = open(File_Name, "w", encoding="utf-8")
    for t in Works:
        file.write(t["title"] + "|" + str(t["done"]) + "|" + t["date"] + "\n")
    file.close()
