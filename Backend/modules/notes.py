#This is a note writing script for managing notes
#Imported libraries neccessary for the development of note managment system
#_____________________________________________________________________________________________
import Backend.modules.utils as utils
#_____________________________________________________________________________________________


#The add_note function allows users to create a new note by providing a title and content.
#_____________________________________________________________________________________________
def add_note():
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    date = utils.get_current_timestamp()  # Get current date and time
    note = {
        "title": title,
        "content": content,
        "date": date
    }
    # Load existing notes
    notes = utils.load_items("data/notes.json")
    # Add the new note
    notes.append(note)
    # Save notes
    utils.save_items("data/notes.json", notes)
    return add_note
'''End add_note function'''
#_____________________________________________________________________________________________


#The view_all_notes function displays all notes in the system.
#_____________________________________________________________________________________________
def view_all_notes():
    notes = utils.load_items("data/notes.json")
    for note in notes:
        print(f"Title: {note['title']}, Date: {note['date']}\nContent: {note['content']}\n")
    if not notes:
        print("No notes found.")
    return notes
'''End view_all_notes function'''
#_____________________________________________________________________________________________


#The view_note_by_date function allows users to view notes created on a specific date.
#_____________________________________________________________________________________________
def view_note_by_date():
    date_to_view = input("Enter date in format: yyyy-mm-dd: ")
    notes = utils.load_items("data/notes.json")
    found = False
    for note in notes:
        if note['date'].startswith(date_to_view):
            print(f"Title: {note['title']}, Date: {note['date']}\nContent: {note['content']}\n")
            found = True
    if not found:
        print(f"No notes found for {date_to_view}")
    return notes
'''End view_note_by_date function'''
#_____________________________________________________________________________________________


#The delete_note function allows users to remove a note by title.
#_____________________________________________________________________________________________
def delete_note():
    note_to_remove = input("Enter the note title you want to delete: ").lower()
    notes = utils.load_items("data/notes.json")
    notes_to_keep = [note for note in notes if note['title'].lower() != note_to_remove]
    utils.save_items("data/notes.json", notes_to_keep)
    if note_to_remove not in [note['title'].lower() for note in notes]:
        print(f"Note {note_to_remove} not found.")
    else:
        print(f"Note {note_to_remove} deleted.")
    return notes
'''End delete_note function'''
#_____________________________________________________________________________________________


#The edit_note function allows users to modify an existing note.
#_____________________________________________________________________________________________
def edit_note():
    note_to_edit = input("Enter the note title you want to edit: ").lower()
    notes = utils.load_items("data/notes.json")
    for note in notes:
        if note['title'].lower() == note_to_edit:
            new_content = input("Enter the new content for the note: ")
            note['content'] = new_content
            utils.save_items("data/notes.json", notes)
            print(f"Note {note_to_edit} updated.")
            return notes
        else:
            print(f"Note {note_to_edit} not found.")
    return notes
'''End edit_note function'''
#_____________________________________________________________________________________________


#The main function serves as the entry point for the notes management system.
#_____________________________________________________________________________________________
def main():
    print("Notes management system")
    while True:
        print("Select your option")
        print("_"*20)
        print("1. Add note")
        print("2. View note by date")
        print("3. View all notes")
        print("4. Delete note")
        print("5. Edit note")
        print("0. Exit")
        choice = input()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_note_by_date()
        elif choice == "3":
            view_all_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            edit_note()
        elif choice == "0":
            break
        else:
            print("Invalid input")
        return main()
'''End main function'''
#_____________________________________________________________________________________________
