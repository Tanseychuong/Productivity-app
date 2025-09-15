# Web-friendly journal management functions for Flask integration

import os
from typing import List, Dict, Tuple
from . import utils

os.makedirs("Backend/data", exist_ok=True)

def add_journal_data(title: str, content: str) -> Tuple[bool, str]:
    """Add a new journal entry. Returns (success, message)."""
    try:
        if not title.strip() or not content.strip():
            return False, "Title and content are required"
        
        entry_date = utils.get_current_timestamp()
        entry = {
            "title": title.strip(),
            "content": content.strip(),
            "date": entry_date
        }
        
        journal_entries = utils.load_items("Backend/data/journals.json")
        journal_entries.append(entry)
        utils.save_items_with_backup("Backend/data/journals.json", journal_entries)
        return True, "Journal entry added successfully"
    except Exception as e:
        return False, f"Error adding journal entry: {str(e)}"

def get_all_journals() -> List[Dict]:
    """Get all journal entries."""
    return utils.load_items("Backend/data/journals.json")

def delete_journal_by_index(index: int) -> Tuple[bool, str]:
    """Delete a journal entry by index. Returns (success, message)."""
    try:
        journal_entries = utils.load_items("Backend/data/journals.json")
        if 0 <= index < len(journal_entries):
            deleted_entry = journal_entries.pop(index)
            utils.save_items_with_backup("Backend/data/journals.json", journal_entries)
            return True, f'Journal entry "{deleted_entry["title"]}" deleted successfully'
        else:
            return False, "Journal entry not found"
    except Exception as e:
        return False, f"Error deleting journal entry: {str(e)}"

def update_journal_by_index(index: int, title: str, content: str) -> Tuple[bool, str]:
    """Update a journal entry by index. Returns (success, message)."""
    try:
        journal_entries = utils.load_items("Backend/data/journals.json")
        if 0 <= index < len(journal_entries):
            if not title.strip() or not content.strip():
                return False, "Title and content are required"
            
            journal_entries[index] = {
                "title": title.strip(),
                "content": content.strip(),
                "date": journal_entries[index]["date"]  # Keep original date
            }
            utils.save_items_with_backup("Backend/data/journals.json", journal_entries)
            return True, f"Journal entry updated successfully"
        else:
            return False, "Journal entry not found"
    except Exception as e:
        return False, f"Error updating journal entry: {str(e)}"