import json

# Load tasks from file if exists
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

def add_task(task_name):
    tasks.append({"task": task_name, "done": False})
    print(f"Added task: {task_name}")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")
    print()

def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print(f"Marked '{tasks[task_index]['task']}' as done!")
    else:
        print("Invalid task number!")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number!")

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Main Program Loop
print("Welcome to To-Do List Manager!")
while True:
    print("\nOptions: 1.Add  2.View  3.Mark Done  4.Delete  5.Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        task = input("Enter task name: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter task number to mark done: ")) - 1
        mark_done(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        save_tasks()
        print("Tasks saved to tasks.json. Goodbye!")
        break
    else:
        print("Invalid option, try again!")
