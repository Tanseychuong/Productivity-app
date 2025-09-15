from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import CSRFProtect
import os
import secrets
import Backend.modules.contacts as contacts_module
import Backend.modules.journals as journals_module
import Backend.modules.notes as notes_module
import Backend.modules.tasks as tasks_module
from Backend.modules import utils

app = Flask(__name__)

# Security configuration
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
csrf = CSRFProtect(app)

# Configure Flask for Replit environment
app.config['DEBUG'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None  # No time limit for CSRF tokens

@app.route('/')
def home():
    """Main dashboard page"""
    return render_template('home.html')

# Contact routes
@app.route('/contacts')
def contacts():
    """Display all contacts"""
    from Backend.modules.contacts_web import get_all_contacts
    contact_list = get_all_contacts()
    return render_template('contacts.html', contacts=contact_list)

@app.route('/contacts/add', methods=['GET', 'POST'])
def add_contact():
    """Add a new contact"""
    if request.method == 'POST':
        from Backend.modules.contacts_web import add_contact_data
        
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        phone = request.form['phone'].strip()
        email = request.form['email'].strip()
        
        success, message = add_contact_data(first_name, last_name, phone, email)
        if success:
            flash(message, 'success')
            return redirect(url_for('contacts'))
        else:
            flash(message, 'error')
            return redirect(url_for('add_contact'))
    
    return render_template('add_contact.html')

@app.route('/contacts/search', methods=['GET', 'POST'])
def search_contacts():
    """Search contacts"""
    if request.method == 'POST':
        from Backend.modules.contacts_web import search_contacts_web
        
        search_term = request.form['search_term'].strip()
        success, message, results = search_contacts_web(search_term)
        
        if success:
            if results:
                flash(message, 'success')
                return render_template('contacts_search_results.html', contacts=results, search_term=search_term)
            else:
                flash(message, 'info')
                return render_template('contacts_search_results.html', contacts=[], search_term=search_term)
        else:
            flash(message, 'error')
            return redirect(url_for('contacts'))
    
    return render_template('contacts_search.html')

@app.route('/contacts/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    """Edit a contact"""
    from Backend.modules.contacts_web import get_all_contacts, update_contact_by_index
    
    contacts = get_all_contacts()
    if contact_id < 0 or contact_id >= len(contacts):
        flash('Contact not found', 'error')
        return redirect(url_for('contacts'))
    
    contact = contacts[contact_id]
    
    if request.method == 'POST':
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        phone = request.form['phone'].strip()
        email = request.form['email'].strip()
        
        success, message = update_contact_by_index(contact_id, first_name, last_name, phone, email)
        if success:
            flash(message, 'success')
            return redirect(url_for('contacts'))
        else:
            flash(message, 'error')
            return render_template('edit_contact.html', contact=contact, contact_id=contact_id)
    
    return render_template('edit_contact.html', contact=contact, contact_id=contact_id)

@app.route('/contacts/undo', methods=['POST'])
def undo_contacts():
    """Undo last contacts operation"""
    from Backend.modules.contacts_web import undo_contacts_web
    
    success, message = undo_contacts_web()
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('contacts'))

@app.route('/contacts/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    """Delete a contact"""
    from Backend.modules.contacts_web import delete_contact_by_index
    
    success, message = delete_contact_by_index(contact_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('contacts'))

# Journal routes
@app.route('/journals')
def journals():
    """Display all journal entries"""
    from Backend.modules.journals_web import get_all_journals
    journal_entries = get_all_journals()
    return render_template('journals.html', journals=journal_entries)

@app.route('/journals/add', methods=['GET', 'POST'])
def add_journal():
    """Add a new journal entry"""
    if request.method == 'POST':
        from Backend.modules.journals_web import add_journal_data
        
        title = request.form['title'].strip()
        content = request.form['content'].strip()
        
        success, message = add_journal_data(title, content)
        if success:
            flash(message, 'success')
            return redirect(url_for('journals'))
        else:
            flash(message, 'error')
            return redirect(url_for('add_journal'))
    
    return render_template('add_journal.html')

@app.route('/journals/edit/<int:journal_id>', methods=['GET', 'POST'])
def edit_journal(journal_id):
    """Edit a journal entry"""
    from Backend.modules.journals_web import get_all_journals, update_journal_by_index
    
    journals_list = get_all_journals()
    if journal_id < 0 or journal_id >= len(journals_list):
        flash('Journal entry not found', 'error')
        return redirect(url_for('journals'))
    
    journal = journals_list[journal_id]
    
    if request.method == 'POST':
        title = request.form['title'].strip()
        content = request.form['content'].strip()
        
        success, message = update_journal_by_index(journal_id, title, content)
        if success:
            flash(message, 'success')
            return redirect(url_for('journals'))
        else:
            flash(message, 'error')
            return render_template('edit_journal.html', journal=journal, journal_id=journal_id)
    
    return render_template('edit_journal.html', journal=journal, journal_id=journal_id)

@app.route('/journals/delete/<int:journal_id>', methods=['POST'])
def delete_journal(journal_id):
    """Delete a journal entry"""
    from Backend.modules.journals_web import delete_journal_by_index
    
    success, message = delete_journal_by_index(journal_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('journals'))

# Notes routes
@app.route('/notes')
def notes():
    """Display all notes"""
    from Backend.modules.notes_web import get_all_notes
    note_list = get_all_notes()
    return render_template('notes.html', notes=note_list)

@app.route('/notes/add', methods=['GET', 'POST'])
def add_note():
    """Add a new note"""
    if request.method == 'POST':
        from Backend.modules.notes_web import add_note_data
        
        title = request.form['title'].strip()
        content = request.form['content'].strip()
        
        success, message = add_note_data(title, content)
        if success:
            flash(message, 'success')
            return redirect(url_for('notes'))
        else:
            flash(message, 'error')
            return redirect(url_for('add_note'))
    
    return render_template('add_note.html')

@app.route('/notes/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    """Edit a note"""
    from Backend.modules.notes_web import get_all_notes, update_note_by_index
    
    notes_list = get_all_notes()
    if note_id < 0 or note_id >= len(notes_list):
        flash('Note not found', 'error')
        return redirect(url_for('notes'))
    
    note = notes_list[note_id]
    
    if request.method == 'POST':
        title = request.form['title'].strip()
        content = request.form['content'].strip()
        
        success, message = update_note_by_index(note_id, title, content)
        if success:
            flash(message, 'success')
            return redirect(url_for('notes'))
        else:
            flash(message, 'error')
            return render_template('edit_note.html', note=note, note_id=note_id)
    
    return render_template('edit_note.html', note=note, note_id=note_id)

@app.route('/notes/date', methods=['GET', 'POST'])
def notes_by_date():
    """View notes by date"""
    if request.method == 'POST':
        from Backend.modules.notes_web import get_notes_by_date
        
        target_date = request.form['date'].strip()
        success, message, results = get_notes_by_date(target_date)
        
        if success:
            if results:
                flash(message, 'success')
                return render_template('notes_date_results.html', notes=results, date=target_date)
            else:
                flash(message, 'info')
                return render_template('notes_date_results.html', notes=[], date=target_date)
        else:
            flash(message, 'error')
            return redirect(url_for('notes'))
    
    return render_template('notes_date_search.html')

@app.route('/notes/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    """Delete a note"""
    from Backend.modules.notes_web import delete_note_by_index
    
    success, message = delete_note_by_index(note_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('notes'))

# Tasks routes
@app.route('/tasks')
def tasks():
    """Display all tasks"""
    from Backend.modules.tasks_web import get_all_tasks
    task_list = get_all_tasks()
    return render_template('tasks.html', tasks=task_list)

@app.route('/tasks/add', methods=['GET', 'POST'])
def add_task():
    """Add a new task"""
    if request.method == 'POST':
        from Backend.modules.tasks_web import add_task_data
        
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        due_date = request.form['due_date']
        
        success, message = add_task_data(name, description, due_date)
        if success:
            flash(message, 'success')
            return redirect(url_for('tasks'))
        else:
            flash(message, 'error')
            return redirect(url_for('add_task'))
    
    return render_template('add_task.html')

@app.route('/tasks/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed"""
    from Backend.modules.tasks_web import complete_task_by_index
    
    success, message = complete_task_by_index(task_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('tasks'))

@app.route('/tasks/today')
def tasks_today():
    """View today's tasks"""
    from Backend.modules.tasks_web import get_today_tasks
    
    success, message, today_tasks = get_today_tasks()
    if success:
        if today_tasks:
            flash(message, 'success')
        else:
            flash(message, 'info')
        return render_template('tasks_today.html', tasks=today_tasks)
    else:
        flash(message, 'error')
        return redirect(url_for('tasks'))

@app.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Edit a task"""
    from Backend.modules.tasks_web import get_task_by_index, update_task_by_index
    
    success, message, task = get_task_by_index(task_id)
    if not success:
        flash(message, 'error')
        return redirect(url_for('tasks'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description'] 
        due_date = request.form['due_date']
        
        success, message = update_task_by_index(task_id, name, description, due_date)
        if success:
            flash(message, 'success')
            return redirect(url_for('tasks'))
        else:
            flash(message, 'error')
            return render_template('edit_task.html', task=task, task_id=task_id)
    
    return render_template('edit_task.html', task=task, task_id=task_id)

@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task"""
    from Backend.modules.tasks_web import delete_task_by_index
    
    success, message = delete_task_by_index(task_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    # Configure for Replit environment - bind to all interfaces and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)