from SQLiteDatabase.db import Database
from tkinter import messagebox

db = Database("BelgiumCampus.db")

class Delete:

    def delete_student(self, sms_app, StudentId):
        confirm = messagebox.askquestion("Confirm", f"Are you sure you want to delete student No. {StudentId}?")

        if confirm != "yes":
            return
        try:
            db.delete_student(StudentId)
            messagebox.showinfo("Success", f"Student No.{StudentId} Deleted")
            sms_app.pop_student_list()
        except Exception as e:
            messagebox.showerror("Error", f"Can't delete student: {e}")



    def delete_lecturer(self, sms_app, LecturerId):
        confirm = messagebox.askquestion("Confirm", f"Are you sure you want to delete Lecturer No. {LecturerId}?")

        if confirm != "yes":
            return
        try:
            db.delete_lecturer(LecturerId)
            messagebox.showinfo("Success", f"Lecturer No.{LecturerId} Deleted")
            sms_app.pop_lecturer_list()
        except Exception as e:
            messagebox.showerror("Error", f"Can't delete lecturer: {e}")

