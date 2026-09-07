import json
import sys
from datetime import datetime
from tabulate import tabulate

file_path = 'data.json'

def load_data(file_path = file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(task_list):
    with open(file_path, 'w') as file:
        json.dump(task_list, file, indent=4)

def add_task(task_list, description):
    task_counter = len(task_list) + 1
    task = {
        "id": task_counter,
        "description": description,
        "status": "to-do", 
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    task_list.append(task)
    save_data(task_list)
    print(tabulate([task], headers="keys", tablefmt="grid"))

def update_task(task_list, task_id, new_description):
    for task in task_list:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(task_list)
            print(tabulate([task], headers="keys", tablefmt="grid"))
            return
    print(f"Task ID {task_id} not found.")

def delete_task(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            task_list.remove(task)
            save_data(task_list)
            print(f"Task ID {task_id} deleted.")
            return
    print(f"Task ID {task_id} not found.")

def mark_task_done(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            task['status'] = "done"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(task_list)
            print(tabulate([task], headers="keys", tablefmt="grid"))
            return
    print(f"Task ID {task_id} not found.")

def mark_task_in_progress(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            task['status'] = "in-progress"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(task_list)
            print(tabulate([task], headers="keys", tablefmt="grid"))
            return
    print(f"Task ID {task_id} not found.") 

def list_done(task_list):
    done_tasks = [task for task in task_list if task['status'] == "done"]
    if not done_tasks:
        print("No done tasks found.")
        return
    print(tabulate(done_tasks, headers="keys", tablefmt="grid"))

def list_in_progress(task_list):
    in_progress_tasks = [task for task in task_list if task['status'] == "in-progress"]
    if not in_progress_tasks:
        print("No in-progress tasks found.")
        return
    print(tabulate(in_progress_tasks, headers="keys", tablefmt="grid"))

def list_to_do(task_list):
    to_do_tasks = [task for task in task_list if task['status'] == "to-do"]
    if not to_do_tasks:
        print("No to-do tasks found.")
        return
    print(tabulate(to_do_tasks, headers="keys", tablefmt="grid"))

def list_tasks(task_list):
    if not task_list:
        print("No tasks found.")
        return
    print(tabulate(task_list, headers="keys", tablefmt="grid"))

def menu(task_list):
    if len(sys.argv) >= 3 and sys.argv[1] == "add":
        description = sys.argv[2]
        add_task(task_list, description)
    elif len(sys.argv) >= 2 and sys.argv[1] == "list":
        list_tasks(task_list)
    elif len(sys.argv) >= 3 and sys.argv[1] == "update":
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        update_task(task_list, task_id, new_description)
    elif len(sys.argv) >= 3 and sys.argv[1] == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_list, task_id)
    elif len(sys.argv) >= 3 and sys.argv[1] == "mark-done":
        task_id = int(sys.argv[2])
        mark_task_done(task_list, task_id)
    elif len(sys.argv) >= 3 and sys.argv[1] == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_task_in_progress(task_list, task_id)
    elif len(sys.argv) >= 2 and sys.argv[1] == "list-done":
        list_done(task_list)
    elif len(sys.argv) >= 2 and sys.argv[1] == "list-in-progress":
        list_in_progress(task_list)
    elif len(sys.argv) >= 2 and sys.argv[1] == "list-to-do":
        list_to_do(task_list)
    else:
        print("Invalid command. Usage:")
        print("  python main.py add <description>")
        print("  python main.py list")
        print("  python main.py update <task_id> <new_description>")
        print("  python main.py delete <task_id>")
        print("  python main.py mark-done <task_id>")
        print("  python main.py mark-in-progress <task_id>")
        print("  python main.py list-done")
        print("  python main.py list-in-progress")
        print("  python main.py list-to-do")

if __name__ == "__main__":
    task_list = load_data()
    menu(task_list)