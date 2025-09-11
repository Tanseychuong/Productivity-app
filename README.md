# Smart Personal Schedule

Smart Personal Schedule is a command-line Python application that helps you manage your contacts, journal entries, notes, and tasks efficiently. All data is stored in JSON files for easy access and portability.

## Features

- **Contact Management**
  - Add, delete, update, search, and view contacts.
- **Journal Management**
  - (Feature placeholder: Implemented in `journal.py`)
- **Notes Management**
  - Add, view (by date or all), and delete notes.
- **Task Management**
  - Add, view, delete, and mark tasks as completed.
  - View today's tasks.
- **Utilities**
  - Get the current timestamp and other helper functions.

## File Structure

```
smart_personal_schedule/
│
├── contacts.py         # Contact management functions
├── journal.py          # Journal management functions
├── notes.py            # Notes management functions
├── tasks.py            # Task management functions
├── utils.py            # Utility/helper functions
├── data/
│   ├── contacts.json   # Contacts data storage
│   ├── journal.json    # Journal entries storage
│   ├── notes.json      # Notes storage
│   └── tasks.json      # Tasks storage
├── README.md           # Project documentation
└── ...                 # Other files and folders
```

## Getting Started

1. **Clone the repository**
2. **Install Python 3.x**
3. **Run the desired module** (e.g., `python contacts.py`)

## Usage

Each module provides a command-line menu for managing its respective data. Follow the on-screen prompts to add, view, update, or delete entries.
