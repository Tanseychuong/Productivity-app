#Creating a python file for contact managment for smart schedule
# The implementation includes functions to add, delete, view, search, and update contacts.


'''#The imported modules necessary for contact management
#____________________________________________________________________________________________________
from . import utils  #importing utils module for handling JSON data
#____________________________________________________________________________________________________


#Function to add contact to the contact file
#____________________________________________________________________________________________________
def add_contact():
    name = input("Enter first name: ") #getting firstname from the user.
    lastname = input("Enter last name: ")
    phone_num = input("Enter phone number: ")
    email = input("Enter the email: ")

    while not utils.validate_email(email):  # Validate email format
        email = input("Enter a valid email: or enter 0000 to skip: ")
        if email == "0000":
            email = "Not provided"
            break
    # Load existing contacts
    contacts = utils.load_items("data/contacts.json")
    # Add new contact
    contacts.append({
        "first_name": name,
        "last_name": lastname,
        "phone": phone_num,
        "email": email
    })

    # Save contacts
    utils.save_items("data/contacts.json", contacts)
# End of add_contact
#____________________________________________________________________________________________________


#The function for deleting contact from the contact file
#____________________________________________________________________________________________________
def delete_contact():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    phone_num = input("Enter the phone number: ")
    email = input("Enter the email: ")
    # Validate email format
    while "@" not in email or "." not in email:
        email = input("Enter a valid email: ")
    # Load existing contacts
    contacts = utils.load_items("data/contacts.json")
    # Remove matching contact(s)
    new_contacts = [
        c for c in contacts
        if not (
            c["first_name"] == first_name and
            c["last_name"] == last_name and
            c["phone"] == phone_num and
            c["email"] == email
        )
    ]
    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        utils.save_items("data/contacts.json", new_contacts)
        print("Contact deleted.")
    return delete_contact
# End of delete_contact
#____________________________________________________________________________________________________



# Function to view all contacts
#____________________________________________________________________________________________________
def view_all_contacts():
    contacts = utils.load_items("data/contacts.json")  # Load contacts from the file
    for contact in contacts:
        print(f"Name: {contact['first_name']} {contact['last_name']}, Phone: {contact['phone']}, Email: {contact['email']}")
# This function is not called in the main loop, but can be used to view all contacts

def search_contact():
    search_name = input("Enter the name to search: ")
    contacts = utils.load_items("data/contacts.json")  # Load contacts from the file
    found_contacts = [
        contact for contact in contacts
        if search_name.lower() in contact["first_name"].lower() or
            search_name.lower() in contact["last_name"].lower()
        ]
    if found_contacts:
        for contact in found_contacts:
            print(f"Found: {contact['first_name']} {contact['last_name']}")
    else:
        print("No contact found.")
    return search_contact
# The end of search_contact function
#_________________________________________________________________________________________________


# The function to update contact information
#__________________________________________________________________________________________________
def update_contact():
    first_name = input("Enter the first name of the contact to update: ")
    last_name = input("Enter the last name of the contact to update: ")
    phone_num = input("Enter the new phone number: ")
    email = input("Enter the new email: ")
    # Load existing contacts
    contacts = utils.load_items("data/contacts.json")  # Load contacts from the file
    # Validate email format
    if not utils.validate_email(email):
        email = input("Enter a valid email: ")  # Ensure the email is valid format

    # Check if contact exists
    if not any(contact["first_name"] == first_name and contact["last_name"] == last_name for contact in contacts):
        print("Contact not found.")
        return

    # Find and update the contact
    for contact in contacts:
        if (contact["first_name"] == first_name and
                contact["last_name"] == last_name):
            contact["phone"] = phone_num
            contact["email"] = email
            break
    else:
        print("Contact not found.")
        return

    # Save updated contacts
    utils.save_items("data/contacts.json", contacts)  # Save updated contacts to the file
    print("Contact updated.")
    return update_contact()
# End of the update_contact function
#__________________________________________________________________________________________________



# Main function to run the contact management system
#__________________________________________________________________________________________________
def main():
    print("Contact Management")
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View All Contacts")
        print("4. Search Contact")
        print("5. Update Contact")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            view_all_contacts()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            update_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
# End of the main function
#__________________________________________________________________________________________________'''


import os
from typing import List, Dict
from tabulate import tabulate
from . import utils

os.makedirs("data", exist_ok=True)  # Ensure data directory exists

def add_contact() -> None:
    """Add a new contact to the contacts.json file."""
    name = utils.validate_non_empty_string(input("Enter first name: "), "Enter first name: ")
    lastname = utils.validate_non_empty_string(input("Enter last name: "), "Enter last name: ")
    phone_num = utils.validate_non_empty_string(input("Enter phone number: "), "Enter phone number: ")
    email = input("Enter the email: ")

    while not utils.validate_email(email):
        email = input("Enter a valid email or enter 0000 to skip: ")
        if email == "0000":
            email = "Not provided"
            break

    contacts: List[Dict[str, str]] = utils.load_items("data/contacts.json")
    contacts.append({
        "first_name": name,
        "last_name": lastname,
        "phone": phone_num,
        "email": email
    })
    utils.save_items("data/contacts.json", contacts)
    print("Contact added successfully.")

def delete_contact() -> None:
    """Delete a contact from the contacts.json file."""
    first_name = utils.validate_non_empty_string(input("Enter the first name: "), "Enter the first name: ")
    last_name = utils.validate_non_empty_string(input("Enter the last name: "), "Enter the last name: ")
    phone_num = utils.validate_non_empty_string(input("Enter the phone number: "), "Enter the phone number: ")
    email = input("Enter the email: ")
    while not utils.validate_email(email):
        email = input("Enter a valid email: ")
    
    contacts: List[Dict[str, str]] = utils.load_items("data/contacts.json")
    new_contacts = [
        c for c in contacts
        if not (
            c["first_name"].lower() == first_name.lower() and
            c["last_name"].lower() == last_name.lower() and
            c["phone"] == phone_num and
            c["email"] == email
        )
    ]
    if len(new_contacts) == len(contacts):
        print("Contact not found.")
        return
    
    confirm = input("Are you sure you want to delete this contact? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.")
        return
    
    utils.save_items("data/contacts.json", new_contacts)
    print("Contact deleted.")

def view_all_contacts() -> None:
    """View all contacts, with optional sorting."""
    contacts: List[Dict[str, str]] = utils.load_items("data/contacts.json")
    if not contacts:
        print("No contacts found.")
        return
    
    sort_by = input("Sort by (1. First Name, 2. Last Name, 3. Email, 0. None): ")
    if sort_by == "1":
        contacts.sort(key=lambda x: x["first_name"].lower())
    elif sort_by == "2":
        contacts.sort(key=lambda x: x["last_name"].lower())
    elif sort_by == "3":
        contacts.sort(key=lambda x: x["email"].lower())
    
    table = [[c["first_name"], c["last_name"], c["phone"], c["email"]] for c in contacts]
    print(tabulate(table, headers=["First Name", "Last Name", "Phone", "Email"], tablefmt="grid"))

def search_contact() -> None:
    """Search contacts by name, phone, or email."""
    search_term = utils.validate_non_empty_string(input("Enter name, phone, or email to search: "), "Enter name, phone, or email: ").lower()
    contacts: List[Dict[str, str]] = utils.load_items("data/contacts.json")
    found_contacts = [
        contact for contact in contacts
        if (search_term in contact["first_name"].lower() or
            search_term in contact["last_name"].lower() or
            search_term in contact["phone"] or
            search_term in contact["email"].lower())
    ]
    if found_contacts:
        table = [[c["first_name"], c["last_name"], c["phone"], c["email"]] for c in found_contacts]
        print(tabulate(table, headers=["First Name", "Last Name", "Phone", "Email"], tablefmt="grid"))
    else:
        print("No contact found.")

def update_contact() -> None:
    """Update a contact's phone or email."""
    first_name = utils.validate_non_empty_string(input("Enter the first name of the contact to update: "), "冥System: Enter the first name: ")
    last_name = utils.validate_non_empty_string(input("Enter the last name of the contact to update: "), "冥System: Enter the last name: ")
    phone_num = utils.validate_non_empty_string(input("Enter the new phone number: "), "冥System: Enter the new phone number: ")
    email = input("Enter the new email: ")
    while not utils.validate_email(email):
        email = input("Enter a valid email: ")
    
    contacts: List[Dict[str, str]] = utils.load_items("data/contacts.json")
    if not any(c["first_name"].lower() == first_name.lower() and c["last_name"].lower() == last_name.lower() for c in contacts):
        print("Contact not found.")
        return
    
    for contact in contacts:
        if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
            contact["phone"] = phone_num
            contact["email"] = email
            break
    
    utils.save_items("data/contacts.json", contacts)
    print("Contact updated.")

def main() -> None:
    """Run the contact management system."""
    print("Contact Management")
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View All Contacts")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Undo Last Change")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            view_all_contacts()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            utils.undo_last_change("data/contacts.json")
        elif choice == "0":
            print("Exiting Contact Management.")
            break
        else:
            print("Invalid choice. Please try again.")
# This code is for managing contacts in a simple way, allowing users to add and delete contacts.
# It uses a JSON file to store the contacts, and provides a simple command-line interface for interaction.'''