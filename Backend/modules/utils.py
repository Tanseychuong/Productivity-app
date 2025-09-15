import datetime
import json
import os

#_____________________________________________________________________________________________
def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'''End get_current_timestamp function'''
#_____________________________________________________________________________________________


#_____________________________________________________________________________________________
def load_items(file_path): # Function to load items from a file
    try:
        with open(file_path, "r") as file:
            items = json.load(file) #unpacking the JSON data
        return items
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading items: {e}")
        return []
'''End load_items function'''
#_____________________________________________________________________________________________


# Function to save items to a file
#____________________________________________________________________________________________
def save_items(file_path, items): # Function to save items to a file
    try:
        with open(file_path, "w") as file:
            json.dump(items, file)
    except Exception as e:
        return (f"Error saving items: {e}")
'''End save_items function'''
#_____________________________________________________________________________________________


# Function to validate email format
#_____________________________________________________________________________________________
def validate_email(email): # Function to validate email format
    try:
        if "@" in email and "." in email:
            return True
    except Exception:
        print(f"Error validating email")
    return False
'''End validate_email function'''
#______________________________________________________________________________________________


# Function to validate non-empty string input
#_____________________________________________________________________________________________
def validate_non_empty_string(input_value, prompt):
    """Validate that input is not empty, keep prompting until valid input is provided."""
    while not input_value or input_value.strip() == "":
        input_value = input(prompt)
    return input_value.strip()
'''End validate_non_empty_string function'''
#_____________________________________________________________________________________________


# Function for undo last change 
#_____________________________________________________________________________________________
def create_backup(file_path: str) -> None:
    """Create a backup of the current file before making changes."""
    try:
        backup_path = file_path + ".backup"
        if os.path.exists(file_path):
            import shutil
            shutil.copy2(file_path, backup_path)
    except Exception as e:
        print(f"Error creating backup: {e}")

def undo_last_change(file_path: str) -> bool:
    """Restore the last backup of the specified file."""
    try:
        backup_path = file_path + ".backup"
        if os.path.exists(backup_path):
            import shutil
            shutil.copy2(backup_path, file_path)
            return True
        else:
            print("No backup found to restore.")
            return False
    except Exception as e:
        print(f"Error during undo: {e}")
        return False

def save_items_with_backup(file_path: str, items) -> None:
    """Save items to a file after creating a backup."""
    create_backup(file_path)
    save_items(file_path, items)
'''End undo_last_change function'''
#______________________________________________________________________________________________