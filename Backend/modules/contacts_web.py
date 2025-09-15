# Web-friendly contact management functions for Flask integration
# These functions separate business logic from CLI input/output

import os
from typing import List, Dict, Optional, Tuple
from . import utils

os.makedirs("Backend/data", exist_ok=True)  # Ensure data directory exists

# Core business logic functions that can be used by both CLI and Flask
#____________________________________________________________________________________________________

def add_contact_data(first_name: str, last_name: str, phone: str, email: str = "Not provided") -> Tuple[bool, str]:
    """Add a new contact to the contacts file. Returns (success, message)."""
    try:
        if not first_name.strip() or not last_name.strip() or not phone.strip():
            return False, "First name, last name, and phone are required"
        
        if email and email != "Not provided" and not utils.validate_email(email):
            return False, "Invalid email format"
        
        contacts = utils.load_items("Backend/data/contacts.json")
        contacts.append({
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "phone": phone.strip(),
            "email": email.strip() if email else "Not provided"
        })
        utils.save_items_with_backup("Backend/data/contacts.json", contacts)
        return True, f"Contact {first_name} {last_name} added successfully"
    except Exception as e:
        return False, f"Error adding contact: {str(e)}"

def get_all_contacts() -> List[Dict]:
    """Get all contacts from the contacts file."""
    return utils.load_items("Backend/data/contacts.json")

def delete_contact_by_index(index: int) -> Tuple[bool, str]:
    """Delete a contact by index. Returns (success, message)."""
    try:
        contacts = utils.load_items("Backend/data/contacts.json")
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            utils.save_items_with_backup("Backend/data/contacts.json", contacts)
            return True, f"Contact {deleted_contact['first_name']} {deleted_contact['last_name']} deleted successfully"
        else:
            return False, "Contact not found"
    except Exception as e:
        return False, f"Error deleting contact: {str(e)}"

def search_contacts(search_term: str) -> List[Dict]:
    """Search for contacts by name, phone, or email. Returns list of matching contacts."""
    contacts = utils.load_items("Backend/data/contacts.json")
    return [
        contact for contact in contacts
        if search_term.lower() in contact["first_name"].lower() or
           search_term.lower() in contact["last_name"].lower() or
           search_term.lower() in contact["phone"].lower() or
           search_term.lower() in contact["email"].lower()
    ]

def search_contacts_web(search_term: str) -> Tuple[bool, str, List[Dict]]:
    """Web-friendly search for contacts. Returns (success, message, results with original indices)."""
    try:
        if not search_term.strip():
            return False, "Search term is required", []
        
        all_contacts = utils.load_items("Backend/data/contacts.json")
        results = []
        
        for index, contact in enumerate(all_contacts):
            if (search_term.lower() in contact["first_name"].lower() or
                search_term.lower() in contact["last_name"].lower() or
                search_term.lower() in contact["phone"].lower() or
                search_term.lower() in contact["email"].lower()):
                contact_with_id = contact.copy()
                contact_with_id['original_index'] = index
                results.append(contact_with_id)
        
        if results:
            return True, f"Found {len(results)} contact(s)", results
        else:
            return True, "No contacts found matching your search", []
    except Exception as e:
        return False, f"Error searching contacts: {str(e)}", []

def update_contact_by_index(index: int, first_name: str, last_name: str, phone: str, email: str) -> Tuple[bool, str]:
    """Update a contact by index. Returns (success, message)."""
    try:
        contacts = utils.load_items("Backend/data/contacts.json")
        if 0 <= index < len(contacts):
            if email and not utils.validate_email(email):
                return False, "Invalid email format"
            
            contacts[index] = {
                "first_name": first_name.strip(),
                "last_name": last_name.strip(),
                "phone": phone.strip(),
                "email": email.strip() if email else "Not provided"
            }
            utils.save_items_with_backup("Backend/data/contacts.json", contacts)
            return True, f"Contact updated successfully"
        else:
            return False, "Contact not found"
    except Exception as e:
        return False, f"Error updating contact: {str(e)}"

def undo_contacts_web() -> Tuple[bool, str]:
    """Web-friendly undo last contact operation. Returns (success, message)."""
    try:
        success = utils.undo_last_change("Backend/data/contacts.json")
        if success:
            return True, "Last contact operation has been undone successfully"
        else:
            return False, "No previous operation found to undo"
    except Exception as e:
        return False, f"Error during undo operation: {str(e)}"