import csv
import os

FILENAME = "tasks.csv"

# Create file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Status"])

def add_task():
    task = input("Enter task: ")
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, "Pending"])
    print("Task added!\n")

def view_tasks():
    print("\nYour Tasks:")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row[0]} - {row[1]}")
    print()

def mark_done():
    view_tasks()
    task_no = int(input("Enter task number to mark as done: "))
    tasks = []
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    if 0 < task_no <= len(tasks)-1:
        tasks[task_no][1] = "Done"
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Task marked as done!\n")
    else:
        print("Invalid task number.\n")

def delete_task():
    view_tasks()
    task_no = int(input("Enter task number to delete: "))
    tasks = []
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    if 0 < task_no <= len(tasks)-1:
        removed = tasks.pop(task_no)
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print(f"Task '{removed[0]}' deleted!\n")
    else:
        print("Invalid task number.\n")

# Menu
while True:
    print("=== TaskBuddy ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")