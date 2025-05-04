Student and Lecturer Management System (SMS)
Python Tkinter SQLite

A GUI-based application built with Python’s Tkinter for managing student and lecturer records, with SQLite as the backend database. Supports CRUD operations (Create, Read, Update, Delete) with data validation and error handling.

📌 Features
✅ User-Friendly GUI

Main application window with navigation to student/lecturer management.

Separate forms for adding, updating, and deleting records.

✅ Database Integration

SQLite tables for storing student/lecturer details (e.g., name, ID, course).

Python functions to perform CRUD operations via SQL queries.

✅ Validation & Error Handling

Prevents duplicate/invalid entries.

Graceful error messages for database exceptions.

✅ Optional Extras

Search functionality to filter records.

Sorting options for displayed data.

🛠️ Tech Stack
Frontend: Tkinter (Python’s standard GUI toolkit).

Backend: SQLite3 (lightweight, serverless database).

Language: Python 3.x.

📂 Project Structure
plaintext
sms/  
├── main.py              # Entry point (Tkinter main window)  
├── database.py          # SQLite DB connection & CRUD operations  
├── student_form.py      # Student management GUI  
├── lecturer_form.py     # Lecturer management GUI  
├── data/                # SQLite database file (.db)  
└── README.md            # Project documentation  
🚀 Setup
Clone the repository:

bash
Run the application:

bash
python main.py
📜 License
This project is open-source under the MIT License.
