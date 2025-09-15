# Web-friendly notes management functions for Flask integration

import os
from typing import List, Dict, Tuple
from . import utils

os.makedirs("Backend/data", exist_ok=True)

def add_note_data(title: str, content: str) -> Tuple[bool, str]:
    """Add a new note. Returns (success, message)."""
    try:
        if not title.strip() or not content.strip():
            return False, "Title and content are required"
        
        date = utils.get_current_timestamp()
        note = {
            "title": title.strip(),
            "content": content.strip(),
            "date": date
        }
        
        notes = utils.load_items("Backend/data/notes.json")
        notes.append(note)
        utils.save_items_with_backup("Backend/data/notes.json", notes)
        return True, "Note added successfully"
    except Exception as e:
        return False, f"Error adding note: {str(e)}"

def get_all_notes() -> List[Dict]:
    """Get all notes."""
    return utils.load_items("Backend/data/notes.json")

def delete_note_by_index(index: int) -> Tuple[bool, str]:
    """Delete a note by index. Returns (success, message)."""
    try:
        notes = utils.load_items("Backend/data/notes.json")
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            utils.save_items_with_backup("Backend/data/notes.json", notes)
            return True, f'Note "{deleted_note["title"]}" deleted successfully'
        else:
            return False, "Note not found"
    except Exception as e:
        return False, f"Error deleting note: {str(e)}"

def update_note_by_index(index: int, title: str, content: str) -> Tuple[bool, str]:
    """Update a note by index. Returns (success, message)."""
    try:
        notes = utils.load_items("Backend/data/notes.json")
        if 0 <= index < len(notes):
            if not title.strip() or not content.strip():
                return False, "Title and content are required"
            
            notes[index] = {
                "title": title.strip(),
                "content": content.strip(),
                "date": notes[index]["date"]  # Keep original date
            }
            utils.save_items_with_backup("Backend/data/notes.json", notes)
            return True, f"Note updated successfully"
        else:
            return False, "Note not found"
    except Exception as e:
        return False, f"Error updating note: {str(e)}"

def get_notes_by_date(target_date: str) -> Tuple[bool, str, List[Dict]]:
    """Get notes created on a specific date. Returns (success, message, results with original indices)."""
    try:
        if not target_date.strip():
            return False, "Date is required", []
        
        all_notes = utils.load_items("Backend/data/notes.json")
        matching_notes = []
        
        for index, note in enumerate(all_notes):
            if note['date'].startswith(target_date):
                note_with_id = note.copy()
                note_with_id['original_index'] = index
                matching_notes.append(note_with_id)
        
        if matching_notes:
            return True, f"Found {len(matching_notes)} note(s) for {target_date}", matching_notes
        else:
            return True, f"No notes found for {target_date}", []
    except Exception as e:
        return False, f"Error searching notes by date: {str(e)}", []