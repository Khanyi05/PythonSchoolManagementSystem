from SQLiteDatabase.db import Database
from tkinter import messagebox

db = Database("BelgiumCampus.db")

class Populate:
    def populate_student_list(self, sms_app):
        sms_app.student_list.delete(*sms_app.student_list.get_children())
            # Fetches and populates the Treeview with details
        try:
            data = db.fetch_student()
            if data:
                for row in data:
                    sms_app.student_list.insert("", "end", values=row)
            else:
                messagebox.showinfo("Database","No data found in the Student table.")
        except Exception as e:
            messagebox.showinfo("Database",f"Could not connect to DB: {e}" )


    def populate_lecturer_list(self, sms_app):
        sms_app.lecturer_list.delete(*sms_app.lecturer_list.get_children())
            # Fetches and populates the Treeview with details
        try:
            data = db.fetch_lecturer()
            if data:
                for row in data:
                    sms_app.lecturer_list.insert("", "end", values=row)
            else:
                messagebox.showinfo("Database", "No data found in the Lecturer table.")
        except Exception as e:
            messagebox.showinfo("Database", f"Could not connect to DB: {e}")