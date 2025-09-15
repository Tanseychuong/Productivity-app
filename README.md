Smart Personal Schedule
Overview
Smart Personal Schedule is a command-line Python application that helps users manage their contacts, journal entries, notes, and tasks efficiently. All data is stored in JSON files for easy access and portability.

Current State
Successfully imported from GitHub
Python 3.11 environment configured
All dependencies installed (tabulate)
Application is running as a command-line interface
Data files stored in Backend/data/ directory
Recent Changes (September 15, 2025)
Fixed import path issues in all modules
Added proper package structure with init.py files
Updated requirements.txt with tabulate dependency
Set up workflow to run the application
Configured environment for Replit
Project Architecture
├── app.py                    # Main entry point
├── Backend/
│   ├── __init__.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── utils.py          # Utility functions
│   │   ├── contacts.py       # Contact management
│   │   ├── journals.py       # Journal management
│   │   ├── notes.py          # Notes management
│   │   └── tasks.py          # Task management
│   └── data/
│       ├── contacts.json     # Contact data
│       ├── journals.json     # Journal data
│       ├── notes.json        # Notes data
│       └── tasks.json        # Task data
├── requirements.txt          # Python dependencies
└── replit.md                # Project documentation
Features
Contact Management: Add, delete, update, search, and view contacts
Journal Management: Add, view, edit, and delete journal entries
Notes Management: Add, view by date, and delete notes
Task Management: Add, view, delete, and mark tasks as completed
Data Persistence: All data stored in JSON files
Technical Details
Language: Python 3.11
Dependencies: tabulate (for table formatting)
Data Storage: JSON files
Interface: Command-line interface (CLI)
Architecture: Modular design with separate modules for each feature
User Preferences
Command-line interface preferred for simplicity
JSON data storage for portability
Modular code structure for maintainability
Running the Application
The application runs automatically via the workflow. Users can interact with the CLI through the console output to manage their personal schedule data.
