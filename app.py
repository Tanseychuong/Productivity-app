# main.
# This is the main entry point for the smart personal schedules system.

#The imported modules for the system
#__________________________________________________________________________________________________
import sys
# Ensure the contacts.JSON file exists
import Backend.modules.journals as journals
import Backend.modules.contacts as contacts
import Backend.modules.notes as notes
import Backend.modules.tasks as tasks
'''End of the imported modules'''
#__________________________________________________________________________________________________


#main loop for the contact management system
#__________________________________________________________________________________________________
while True:
    print("Welcome to the smart personal schedules system")
    print("1. Contact Management")
    print("2. Journal Management")
    print("3. Notes Management")
    print("4. Task Management")
    print("0. Exit")


    choice = input("Select menu: ")
    if choice == "1":
        contacts.main()  # Call the main function from contacts.py
    elif choice == "2":
        journals.main()  # Call the main function from journal.py
    elif choice == "3":
        notes.main()  # Call the main function from notes.py
    elif choice == "4":
        tasks.main()  # Call the main function from tasks.py
    elif choice == "0":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
'''End of the main module'''
#__________________________________________________________________________________________________
# This module serves as the entry point for the smart personal 
# schedules system, integrating various management features.