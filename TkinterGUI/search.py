from SQLiteDatabase.db import Database
from tkinter import messagebox

db = Database("BelgiumCampus.db")

class Search:
    def search_student(self, sms_app, search_term):
        try:
            results = db.search_student(search_term)
            # Clear the previous results in the Treeview
            for item in sms_app.search_results_student.get_children():
                sms_app.search_results_student.delete(item)

            if not results:
                messagebox.showinfo("No Results", f"No students found matching {search_term}.")
                return

            # Insert search results into the Treeview
            for result in results:
                sms_app.search_results_student.insert("", "end", values=result)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to search students: {e}")


    def search_lecturer(self, sms_app, search_term):
        try:
            results = db.search_lecturer(search_term)
            # Clear the previous results in the Treeview
            for item in sms_app.search_results_lecturer.get_children():
                sms_app.search_results_lecturer.delete(item)

            if not results:
                messagebox.showinfo("No Results", f"No lecturers found matching {search_term}.")
                return

            # Insert search results into the Treeview
            for result in results:
                sms_app.search_results_lecturer.insert("", "end", values=result)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to search lecturer: {e}")
