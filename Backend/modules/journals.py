# Import necessary libraries for journal management
#____________________________________________________________________________________________________________________________________
from . import utils
#____________________________________________________________________________________________________________________________________


# Add Journal Entry function
#____________________________________________________________________________________________________________________________________
def add_journal_entry():
    title = input("Enter the journal entry title: ")
    content = input("Enter the journal entry content: ")
    entry_date = utils.get_current_timestamp()  # Get current date and time
    entry = {
        "title": title,
        "content": content,
        "date": entry_date
    }
    journal_entries = utils.load_items("data/journal.json") # Load existing journal entries
    journal_entries.append(entry) # Add new entry
    utils.save_items("data/journal.json", journal_entries) # Save updated entries
    print("Journal entry added successfully.")
'''End of add_journal_entry'''
#____________________________________________________________________________________________________________________________________


# View Journal Entries function
#____________________________________________________________________________________________________________________________________
def view_journal_entries():
    journal_entries = utils.load_items("data/journal.json") # Load existing journal entries
    for entry in journal_entries:
        print(f"Title: {entry['title']}, Date: {entry['date']}\nContent: {entry['content']}\n")
    if not journal_entries:
        print("No journal entries found.")
        return []
    return journal_entries
'''End of view_journal_entries'''
#____________________________________________________________________________________________________________________________________


# Edit Journal Entry function
#____________________________________________________________________________________________________________________________________
def edit_journal_entry():
    journal_entries = utils.load_items("data/journal.json") # Load existing journal entries
    if not journal_entries:
        print("No journal entries found.")
        return []
    count = 0
    for entry in journal_entries:
        count += 1 # Increment count for each entry
        print(count, entry["title"])
    
    selected_entry = input("Select the entry to edit: ")
    for each_entry in journal_entries:
        if each_entry["title"] == journal_entries[int(selected_entry)-1]["title"]:
            old_entry = each_entry
            break
    while not selected_entry.isdigit() and 0 <= int(selected_entry) <= len(journal_entries):
        print("Invalid selection. Please enter a valid number.")
        selected_entry = input("Select the entry to edit: ")
    else:
        entry = journal_entries[int(selected_entry)-1]
        selected_content_to_edit = input("Enter the section to edit\n1. Title\n2. Content\n0. Cancel\n")
        try:
            if selected_content_to_edit == "1":
                new_title = input("Enter the new title for the journal entry: ")
                entry['title'] = new_title
                utils.save_items("data/journal.json", journal_entries) # Save updated entries
                print(f"Journal entry titled '{old_entry}' is updated to '{entry['title']}'.")
                return journal_entries


            elif selected_content_to_edit == "2":
                new_content = input("Enter the new content for the journal entry: ")
                entry['content'] = new_content
                utils.save_items("data/journal.json", journal_entries) # Save updated entries
                print(f"Journal entry '{old_entry['title']}' is updated to '{entry['title']}'.")   
                return journal_entries
            elif selected_content_to_edit == "0":
                print("Edit cancelled.")
                return []
            else:
                print("Invalid selection.")
        except IndexError:
            print("Invalid entry selected.")
        return journal_entries
'''End of edit_journal_entry'''
#____________________________________________________________________________________________________________________________________


# Delete Journal Entry function
#____________________________________________________________________________________________________________________________________
def delete_journal_entry():
    title_to_delete = input("Enter the title of the journal entry to delete: ")
    journal_entries = utils.load_items("data/journal.json") # Load existing journal entries
    if not journal_entries:
        print("No journal entries found.")
        return []
    if not any(entry['title'] == title_to_delete for entry in journal_entries):
        print(f"Journal entry '{title_to_delete}' not found.")
        return []
    else:
        journal_entries = [entry for entry in journal_entries if entry['title'] != title_to_delete] # Remove entry with matching title
        print(f"Journal entry '{title_to_delete}' deleted.")
    utils.save_items("data/journal.json", journal_entries) # Save updated entries
    return journal_entries
'''End of delete_journal_entry'''
#____________________________________________________________________________________________________________________________________________


#Main function for journal management
#____________________________________________________________________________________________________________________________________________
def main():
    print("Journal management system")
    while True:
        print("Select your option")
        print("_"*20)
        print("1. Add journal entry")
        print("2. View journal entries")
        print("3. Delete journal entry")
        print("4. Edit journal entry")
        print("0. Exit")
        choice = input()
        if choice == "1":
            add_journal_entry()
        elif choice == "2":
            view_journal_entries()
        elif choice == "3":
            delete_journal_entry()
        elif choice == "4":
            edit_journal_entry()
        elif choice == "0":
            break
        else:
            print("Invalid input")

''' End of main function'''
#____________________________________________________________________________________________________________________________________________
#This module provides a simple journal management system, allowing users to add, view, edit, and delete journal entries.