from SQLiteDatabase.db import Database
from tkinter import messagebox
from SQLiteDatabase.populate import Populate

db = Database("BelgiumCampus.db")


class Add:
    # These methods add Students/ Lecturers to the system by collecting details from the SMSApp instance
    def add_student(self, sms_app):
        # getting details from textboxes
        i = sms_app.student_id_text.get()
        n = sms_app.student_name_text.get()
        s = sms_app.student_surname_text.get()
        d = sms_app.student_dob_text.get()
        c = sms_app.student_course_text.get()
        g = sms_app.gender_selected.get()
        a = sms_app.student_address_text.get()
        co = sms_app.student_contact_num_text.get()
        e = sms_app.student_email_text.get()
        r = sms_app.res_role.get()
        t = sms_app.student_type.get()
        l = sms_app.student_typ.get()

        # Checks if all textboxes are field in and inserts details
        if i and n and s and d and g and a and co and e and r and c and t and l:

            try:
                db.insert_student(i, n, s, d, g, a, co, e, r, c, t, l)
                sms_app.clear_create_student()
                for item in sms_app.student_list.get_children():
                    sms_app.student_list.delete(item)

                # Re-populates the Treeview with new Student details
                Populate().populate_student_list(sms_app)
                messagebox.showinfo("Add","Student Added Successfully")

            except Exception as e:
                messagebox.showerror("Error",f"Failed to add student: {e}")

        else: messagebox.showwarning("Warning","Please fill all fields")


    def add_lecturer(self, sms_app):
        # getting details from textboxes
        i = sms_app.lec_id_text.get()
        n = sms_app.lecturer_name_text.get()
        s = sms_app.lecturer_surname_text.get()
        sp = sms_app.lecturer_specialisation_text.get()
        c = sms_app.lecturer_course_text.get()
        g = sms_app.lecturer_gender.get()
        a = sms_app.lecturer_address_text.get()
        e = sms_app.lecturer_email_text.get()
        t = sms_app.lecturer_title_text.get()
        q = sms_app.lecturer_qual_text.get()
        co = sms_app.lecturer_contact_text.get()

        # Checks if all textboxes are field in and inserts details
        if i and t and n and s and g and a and co and e and q and sp and c:
            try:
                db.insert_lecturer(i,t, n, s, g, a, co, e, q, sp, c)
                sms_app.clear_create_lecturer()
                for item in sms_app.lecturer_list.get_children():
                    # Clearing the Treeview to prepare for population
                    sms_app.lecturer_list.delete(item)

                    # Re-populates the Treeview with new lecturer details
                Populate().populate_lecturer_list(sms_app)

                messagebox.showinfo("Add","Lecturer Added Successfully")

            except Exception as e:
                messagebox.showerror("Error",f"Failed to add Lecturer: {e}")

        else:
            messagebox.showwarning("Warning","Please fill all fields")

