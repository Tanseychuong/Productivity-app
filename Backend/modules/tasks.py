
# Task Management System
# This is a simple task management system that allows users to add, view, and manage tasks.

#The imported modules that are neccessary
#_____________________________________________________________________________________________
import json
import Backend.modules.utils as utils
#_____________________________________________________________________________________________

# The function that adds a new task
#_____________________________________________________________________________________________
def add_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    tasks = utils.load_items("data/tasks.json")
    today = utils.get_current_timestamp()
    today_date = today.split(" ")[0]  # Get only the date part
    year_today = today_date.split("-")[0]  # Get the current year
    task_due_date = input("Enter the task due date (YYYY-MM-DD): ")
    year, month, day = task_due_date.split("-")
    # Validate the date format and values
    while not (1 <= int(month) <= 12 and 1 <= int(day) <= 31 and len(year) == 4 and year_today <= year):
        print("Invalid date format. Please use YYYY-MM-DD.")
        task_due_date = input("Enter the task due date (YYYY-MM-DD): ")
        year, month, day = task_due_date.split("-")
    tasks.append({
        'name': task_name,
        'description': task_description,
        'due_date': task_due_date
    })
    utils.save_items("data/tasks.json", tasks)
    return add_task
#_____________________________________________________________________________________________


# The function that views all tasks
#_____________________________________________________________________________________________
def view_tasks():
    try:
        tasks = utils.load_items("data/tasks.json")
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(f"Task Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print("_" * 20)
    except json.JSONDecodeError:
        print("Error reading tasks file.")
    except FileNotFoundError:
        return ("Error while accessing tasks file.")
#_____________________________________________________________________________________________


# The function that views today's tasks
#_____________________________________________________________________________________________
def view_today_tasks():
    today_date_time = utils.get_current_timestamp()
    today_date = today_date_time.split(" ")
    today = today_date[0]
    tasks = utils.load_items("data/tasks.json")
    today_tasks = [task for task in tasks if task['due_date'] == today]
    if not today_tasks:
        print("No tasks for today.")
    else:
        for task in today_tasks:
            print(f"Task Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print("_" * 20)
    return view_today_tasks
#_____________________________________________________________________________________________


# The function that marks a task as completed
#_____________________________________________________________________________________________
def mark_task_as_completed():
    task_name = input("Enter the name of the task to mark as completed: ")
    tasks = utils.load_items("data/tasks.json")
    for task in tasks:
        if task['name'] == task_name:
            task['completed'] = True
            print("Task marked as completed.")
            return mark_task_as_completed
    else:
        print("Task not found.")
    utils.save_items("data/tasks.json", tasks)
    return mark_task_as_completed
#_____________________________________________________________________________________________


# The function that deletes a task
#_____________________________________________________________________________________________
def delete_task():
    task_name = input("Enter the name of the task to delete: ")
    tasks = utils.load_items("data/tasks.json") # Load existing tasks
    tasks = [task for task in tasks if task['name'] != task_name] # Filter out the task to be deleted
    utils.save_items("data/tasks.json", tasks) # Save updated tasks
    print(f"Task '{task_name}' deleted successfully.")
    return delete_task
#_____________________________________________________________________________________________


# The function that exits the task management system
#_____________________________________________________________________________________________
def main(): # Main function to run the task management system
    print("Task Management")
    while True: # Main loop
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. View Today's Tasks")
        print("5. Mark Task as Completed")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            view_today_tasks()
        elif choice == "5":
            mark_task_as_completed()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
    print("Exiting Task Management System.")
    return main
'''End main function'''
#_____________________________________________________________________________________________