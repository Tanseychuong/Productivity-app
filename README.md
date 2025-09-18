# Smart Personal Schedule

## Overview
Smart Personal Schedule is a command-line Python application that helps users manage their contacts, journal entries, notes, and tasks efficiently. All data is stored in JSON files for easy access and portability.

## Current State
- Successfully imported from GitHub and enhanced with Flask web interface
- Python 3.11 environment configured with Flask framework
- All dependencies installed (Flask, Flask-WTF, WTForms, tabulate)
- **Flask Web Application** running on port 5000 with full feature parity to original CLI
- Data files stored in Backend/data/ directory with consistent path management
- Both CLI and web interfaces available and fully functional

## Recent Changes (September 15, 2025)
- **Flask Web Interface Completed**: Created full-featured Flask web application with complete feature parity to CLI
- **Backend Integration**: Fixed data path inconsistencies and integrated Flask with existing backend modules
- **Security Enhancements**: Added CSRF protection, environment-based secret key, secure POST methods for destructive actions
- **Complete Functionality**: Implemented all CLI features including search, edit/update, undo operations for all modules
- **Template System**: Created comprehensive Bootstrap-based UI with 19 HTML templates covering all functionality
- **Workflow Migration**: Updated from CLI to Flask web interface running on port 5000

## Project Architecture
```
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
```

## Features
- **Contact Management**: Add, delete, update, search, and view contacts
- **Journal Management**: Add, view, edit, and delete journal entries
- **Notes Management**: Add, view by date, and delete notes
- **Task Management**: Add, view, delete, and mark tasks as completed
- **Data Persistence**: All data stored in JSON files

## Technical Details
- Language: Python 3.11
- Dependencies: tabulate (for table formatting)
- Data Storage: JSON files
- Interface: Command-line interface (CLI)
- Architecture: Modular design with separate modules for each feature

## User Preferences
- Command-line interface preferred for simplicity
- JSON data storage for portability
- Modular code structure for maintainability

## Running the Application
The Flask web application runs automatically via the workflow on port 5000. Users can access the modern web interface through their browser to manage contacts, journal entries, notes, and tasks. The original CLI application remains available by running `python app.py` directly.

### Web Interface Features
- **Dashboard**: Central hub with quick access to all modules
- **Contact Management**: Add, edit, delete, search, and undo operations
- **Journal Management**: Add, view, edit, and delete journal entries  
- **Notes Management**: Add, view, edit, delete, and search notes by date
- **Task Management**: Add, view, edit, delete, complete tasks, and view today's tasks
- **Security**: CSRF protection and secure form handling
- **Responsive Design**: Bootstrap-based UI that works on all devices

