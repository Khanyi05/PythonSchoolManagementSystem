from SQLiteDatabase.db import Database
from tkinter import messagebox



db = Database("BelgiumCampus.db")

class Update:
    def update_student(self, sms_app, no):
        i = sms_app.update_student_id_text.get()
        n = sms_app.update_student_name_text.get()
        s = sms_app.update_student_surname_text.get()
        d = sms_app.update_student_dob_text.get()
        c = sms_app.update_student_course_text.get()
        g = sms_app.update_gender_selected.get()
        a = sms_app.update_student_address_text.get()
        co = sms_app.update_student_contact_num_text.get()
        e = sms_app.update_student_email_text.get()
        r = sms_app.update_res_role.get()
        t = sms_app.update_student_type.get()
        l = sms_app.update_student_typ.get()

        # Checks if all textboxes are field in
        if not all ([i, n, s, d, g, a, co, e, r, c, t, l, no]):
            messagebox.showwarning("Warning", "Please fill all fields before updating.")
            return
        try:
            db.update_student(i, n, s, d, g, a, co, e, r, c, t, l, no)
            messagebox.showinfo("Success", f"Student updated successfully!")
            sms_app.pop_student_list()
        except Exception as e:
            messagebox.showerror("Error", f"Can not update student: {e}")


    def update_lecturer(self, sms_app, no):
        # getting details from textboxes
        i = sms_app.update_id_text.get()
        n = sms_app.update_name_text.get()
        s = sms_app.update_surname_text.get()
        sp = sms_app.update_specialisation_text.get()
        c = sms_app.update_course_text.get()
        g = sms_app.update_gender.get()
        a = sms_app.update_address_text.get()
        e = sms_app.update_email_text.get()
        t = sms_app.update_title_text.get()
        q = sms_app.update_qual_text.get()
        co = sms_app.update_contact_text.get()

        # Checks if all textboxes are field in
        if not all([i,t, n, s, g, a, co, e, q, sp, c, no]):
            messagebox.showwarning("Warning", "Please fill all fields before updating.")
            return
        try:
            db.update_lecturer(i,t, n, s, g, a, co, e, q, sp, c, no)
            messagebox.showinfo("Success", f"Lecturer updated successfully!")
            sms_app.pop_lecturer_list()
        except Exception as e:
            messagebox.showerror("Error", f"Can not update Lecturer: {e}")