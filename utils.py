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
    except (FileExistsError, json.JSONDecodeError) as e:
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