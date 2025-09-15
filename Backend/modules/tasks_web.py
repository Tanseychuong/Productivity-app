# Web-friendly tasks management functions for Flask integration

import os
from typing import List, Dict, Tuple
from . import utils

os.makedirs("Backend/data", exist_ok=True)

def add_task_data(name: str, description: str, due_date: str) -> Tuple[bool, str]:
    """Add a new task. Returns (success, message)."""
    try:
        if not name.strip() or not description.strip() or not due_date.strip():
            return False, "All fields are required"
        
        task = {
            'name': name.strip(),
            'description': description.strip(),
            'due_date': due_date.strip(),
            'completed': False
        }
        
        tasks = utils.load_items("Backend/data/tasks.json")
        tasks.append(task)
        utils.save_items_with_backup("Backend/data/tasks.json", tasks)
        return True, "Task added successfully"
    except Exception as e:
        return False, f"Error adding task: {str(e)}"

def get_all_tasks() -> List[Dict]:
    """Get all tasks."""
    return utils.load_items("Backend/data/tasks.json")

def complete_task_by_index(index: int) -> Tuple[bool, str]:
    """Mark a task as completed by index. Returns (success, message)."""
    try:
        tasks = utils.load_items("Backend/data/tasks.json")
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            utils.save_items_with_backup("Backend/data/tasks.json", tasks)
            return True, f'Task "{tasks[index]["name"]}" marked as completed'
        else:
            return False, "Task not found"
    except Exception as e:
        return False, f"Error completing task: {str(e)}"

def delete_task_by_index(index: int) -> Tuple[bool, str]:
    """Delete a task by index. Returns (success, message)."""
    try:
        tasks = utils.load_items("Backend/data/tasks.json")
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            utils.save_items_with_backup("Backend/data/tasks.json", tasks)
            return True, f'Task "{deleted_task["name"]}" deleted successfully'
        else:
            return False, "Task not found"
    except Exception as e:
        return False, f"Error deleting task: {str(e)}"

def get_today_tasks() -> Tuple[bool, str, List[Dict]]:
    """Get tasks due today. Returns (success, message, results with original indices)."""
    try:
        today_date = utils.get_current_timestamp().split(" ")[0]  # Get only the date part
        all_tasks = utils.load_items("Backend/data/tasks.json")
        today_tasks = []
        
        for index, task in enumerate(all_tasks):
            if task['due_date'] == today_date:
                task_with_id = task.copy()
                task_with_id['original_index'] = index
                today_tasks.append(task_with_id)
        
        if today_tasks:
            return True, f"Found {len(today_tasks)} task(s) due today", today_tasks
        else:
            return True, "No tasks due today", []
    except Exception as e:
        return False, f"Error getting today's tasks: {str(e)}", []

def get_task_by_index(index: int) -> Tuple[bool, str, Dict]:
    """Get a task by index. Returns (success, message, task)."""
    try:
        tasks = utils.load_items("Backend/data/tasks.json")
        if 0 <= index < len(tasks):
            return True, "Task found", tasks[index]
        else:
            return False, "Task not found", {}
    except Exception as e:
        return False, f"Error getting task: {str(e)}", {}

def update_task_by_index(index: int, name: str, description: str, due_date: str) -> Tuple[bool, str]:
    """Update a task by index. Returns (success, message)."""
    try:
        if not name.strip() or not description.strip() or not due_date.strip():
            return False, "All fields are required"
        
        tasks = utils.load_items("Backend/data/tasks.json")
        if 0 <= index < len(tasks):
            tasks[index]['name'] = name.strip()
            tasks[index]['description'] = description.strip()
            tasks[index]['due_date'] = due_date.strip()
            utils.save_items_with_backup("Backend/data/tasks.json", tasks)
            return True, f"Task updated successfully"
        else:
            return False, "Task not found"
    except Exception as e:
        return False, f"Error updating task: {str(e)}"