from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import font

from TkinterGUI.add import Add
from TkinterGUI.update import Update
from TkinterGUI.delete import Delete
from TkinterGUI.search import Search
from SQLiteDatabase.populate import Populate



# creating a class which contains widgets
class SMSApp:

    # Set up the constructor for the widgets for the SMSApp class
    def __init__(self, master):
        self.master = master
        self.master.title("Options")
        self.master.geometry("300x250")

        self.selected_role = None  # This is a variable to store the selected role (Student or Lecturer)

        self.current_window = None # Tracking which window is open

        self.student_list = Treeview(self.master)  # Creates a Treeview widget to display a list of students
        self.student_list.pack_forget() # Hides the student Treeview

        self.lecturer_list = Treeview(self.master) # Creates a Treeview widget to display a list of lecturers
        self.lecturer_list.pack_forget() # Hides the lecturer Treeview

        self.set_background_color("")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2= font.Font(family="Helvetica", size=10, weight="bold")


        # Adding a label
        select_option_label = Label(self.master, text="Select Option",font=heading_font , bg="#03045E", fg="#90E0EF", pady= 10)
        select_option_label.pack()

        # Buttons to select the role (Student or Lecturer) and to open crud window and close window
        stu_btn = Button(self.master, text="Student", width=18, bg="#90E0EF", fg="black" ,font= button_font2,command=lambda: self.select_role("Student"))
        stu_btn.pack(pady=10)

        lec_btn = Button(self.master, text="Lecturer", width=18, bg="#90E0EF", fg="black" ,font= button_font2,command=lambda: self.select_role("Lecturer"))
        lec_btn.pack(pady=10)

        crud_btn = Button(self.master, text="Ok", width=18, bg="#90E0EF", fg="black", font=button_font2, command=self.open_crud_window)
        crud_btn.pack(pady=10)

        close_btn = Button(self.master, text="Exit", width=18, bg="#90E0EF", fg="black", font= button_font2, command=self.master.destroy)
        close_btn.pack(pady=10)

    # Function to open the messagebox that shows which role has been selected
    def select_role(self, role):
        self.selected_role = role
        messagebox.showinfo("Role Selected", f"{self.selected_role} Selected")

    # Function to open the CRUD window where the user can perform different crud actions
    def open_crud_window(self):
        self.master.withdraw()

        if self.current_window:
            self.current_window.destroy()

        # Creating a new window for CRUD options
        crud_window = Toplevel(self.master)
        crud_window.geometry("300x350")
        crud_window.title("CRUD Options")
        background = "#03045E"
        crud_window.config(bg=background)

        self.current_window =crud_window


        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        heading_label = Label(crud_window, text="BC Management System", font=heading_font ,bg="#03045E", fg="#90E0EF" ,pady=10)
        heading_label.pack()

        # Checks the selected role and opens the corresponding CRUD option window
        if self.selected_role == "Student":
            Button(crud_window, text="Add Student", command=self.create_student_window, width=20,bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="View all Students", command=self.read_student_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Update Student", command=self.open_student_selection_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Delete Student", command=self.delete_student_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Search", command=self.search_student_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Back", command=self.show_main_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
        elif self.selected_role == "Lecturer":
            Button(crud_window, text="Add Lecturer ", command=self.create_lecturer_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="View all Lecturers", command=self.read_lecturer_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Update Lecturer", command=self.open_lecturer_selection_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Delete Lecturer", command=self.delete_lecturer_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Search", command=self.search_lecturer_window, width=20, bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
            Button(crud_window, text="Back", command=self.show_main_window, width=20,bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)
        else:
            messagebox.askretrycancel("Role Selected", "No role Selected!")
            Button(crud_window, text="Select Role", command=self.show_main_window, width=20,bg="#90E0EF", fg="black", font= button_font2).pack(pady=10)

    # Function to open a window for adding a student
    def create_student_window(self):
        if self.current_window:
            self.current_window.withdraw()

        # Creating a new window for student details
        student_window = Toplevel(self.master)
        student_window.geometry("860x450")
        student_window.title("Student Details")

        self.current_window = student_window
        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")


        # Variables
        self.student_id_text = StringVar()
        self.student_name_text = StringVar()
        self.student_surname_text = StringVar()
        self.student_dob_text = StringVar()
        self.gender_selected = StringVar()
        self.student_address_text = StringVar()
        self.student_contact_num_text = StringVar()
        self.student_email_text = StringVar()
        self.res_role = StringVar()
        self.student_course_text = StringVar()
        self.student_type = StringVar()
        self.student_typ = StringVar()

        # Default options for radio buttons
        self.gender_selected.set("Female")
        self.res_role.set("Yes")
        self.student_type.set("Full-Time")
        self.student_typ.set("Face-Face")

        heading_label = Label(student_window, text="Student Registration Form", font= heading_font)
        heading_label.grid(row=0, column=2)

        # Adding labels and entry boxes for Student details
        student_id = Label(student_window, text="Student ID:", font=("Bold", 12), pady=20, padx=10)
        student_id.grid(row=1, column=0, sticky=W)
        self.id_entry = Entry(student_window, textvariable=self.student_id_text)
        self.id_entry.grid(row=1, column=1)

        student_name = Label(student_window, text="Student Name:", font=("Bold", 12), pady=10, padx=10)
        student_name.grid(row=1, column=4, sticky=W)
        self.name_entry = Entry(student_window, textvariable=self.student_name_text, )
        self.name_entry.grid(row=1, column=5)

        student_surname = Label(student_window, text="Student Surname: ", font=("Bold", 12), pady=10, padx=10)
        student_surname.grid(row=2, column=0, sticky=W)
        self.surname_entry = Entry(student_window, textvariable=self.student_surname_text, )
        self.surname_entry.grid(row=2, column=1)

        student_dob = Label(student_window, text="Date of Birth:", font=("Bold", 12), pady=10, padx=10)
        student_dob.grid(row=2, column=4, sticky=W)
        self.dob_entry = Entry(student_window, textvariable=self.student_dob_text, )
        self.dob_entry.grid(row=2, column=5)

        student_contact = Label(student_window, text="Contact: ", font=("Bold", 12), pady=10, padx=10)
        student_contact.grid(row=3, column=0, sticky=W)
        self.contact_entry = Entry(student_window, textvariable=self.student_contact_num_text, )
        self.contact_entry.grid(row=3, column=1)

        student_address = Label(student_window, text="Address: ", font=("Bold", 12), pady=10, padx=10)
        student_address.grid(row=3, column=4, sticky=W)
        self.address_entry = Entry(student_window, textvariable=self.student_address_text, )
        self.address_entry.grid(row=3, column=5)

        student_gender_label = Label(student_window, text="Gender", font=("Bold", 12), pady=10, padx=10)
        student_gender_label.grid(row=4, column=0, sticky=W)
        female_radio = Radiobutton(student_window, text="Female", variable=self.gender_selected, value="Female")
        female_radio.grid(row=4, column=1)
        male_radio = Radiobutton(student_window, text="Male", variable=self.gender_selected, value="Male")
        male_radio.grid(row=5, column=1)

        student_res = Label(student_window, text="Resident Student ", font=("Bold", 12), pady=10, padx=10)
        student_res.grid(row=4, column=4, sticky=W)
        yes_radio = Radiobutton(student_window, text="Yes", variable=self.res_role, value="Yes")
        yes_radio.grid(row=4, column=5)
        no_radio = Radiobutton(student_window, text="No", variable=self.res_role, value="No")
        no_radio.grid(row=5, column=5)

        student_email = Label(student_window, text="Email Address: ", font=("Bold", 12), pady=10, padx=10)
        student_email.grid(row=6, column=0, sticky=W)
        self.email_entry = Entry(student_window, textvariable=self.student_email_text)
        self.email_entry.grid(row=6, column=1)

        student_course = Label(student_window, text="Course:", font=("Bold", 12), pady=10, padx=10)
        student_course.grid(row=6, column=4, sticky=W)
        self.course_entry = Entry(student_window, textvariable=self.student_course_text, )
        self.course_entry.grid(row=6, column=5)

        student_type = Label(student_window, text="Type ", font=("Bold", 12), pady=10, padx=10)
        student_type.grid(row=7, column=0, sticky=W)
        full_radio = Radiobutton(student_window, text="Full-Time", variable=self.student_type, value="Full-Time",pady=10)
        full_radio.grid(row=7, column=1)
        part_radio = Radiobutton(student_window, text="Part-Time", variable=self.student_type, value="Part-Time",pady=10)
        part_radio.grid(row=8, column=1)

        mode_label = Label(student_window, text="Learning Mode", font=("Bold", 12), pady=10, padx=10)
        mode_label.grid(row=7, column=4, sticky=W)
        face_radio = Radiobutton(student_window, text="Face-Face", variable=self.student_typ, value="Face-Face")
        face_radio.grid(row=7, column=5)
        online_radio = Radiobutton(student_window, text="Online", variable=self.student_typ, value="Online")
        online_radio.grid(row=8, column=5)

        # Buttons to submit the student details and go back to crud window
        submit_btn = Button(student_window, text="Add", bg="#90E0EF", fg="black", font= button_font2, width=10, command=self.add_stu)
        submit_btn.grid(row=11, column=2)

        stu_back_btn = Button(student_window, text="Back", bg="#90E0EF", fg="black", font= button_font2, width=10, command=self.open_crud_window)
        stu_back_btn.grid(row=11, column=3)

    # Function to open a window for viewing student details
    def read_student_window(self):
        if self.current_window:
            self.current_window.withdraw()

        if self.student_list.winfo_ismapped():  # Checks if it is already displayed data in the Treeview
            return

        read_window = Toplevel(self.master)
        read_window.geometry("700x450")
        read_window.title("View Details")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = read_window


       # Treeview to display the student details
        self.student_list = ttk.Treeview(read_window, columns=("No",
                                                               "StudentId",
                                                               "Name", "Surname",
                                                               "DOB", "Gender",
                                                               "Address", "Contact",
                                                               "Email", "Resident",
                                                               "Course", "Student Type",
                                                               "Learning Mode"), show='headings',height=15)

        for col in self.student_list["columns"]:
            self.student_list.heading(col, text=col)
            self.student_list.column(col, width=100, anchor='center')
        self.student_list.pack(pady=10)

        # Buttons to read the student details and to navigate back to the crud window
        view_btn = Button(read_window, text="View",width=10,bg="#90E0EF", fg="black", font= button_font2, command=self.pop_student_list)
        view_btn.pack(pady=10)
        read_s_back_btn = Button(read_window, text="Back", width=10,bg="#90E0EF", fg="black", font= button_font2, command=self.open_crud_window)
        read_s_back_btn.pack(pady=10)

    # Function to open a window for updating student details
    def update_student_window(self, student_info):
        if self.current_window:
            self.current_window.withdraw()

        update_window = Toplevel(self.master)
        update_window.geometry("860x450")
        update_window.title("Update Details")
        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = update_window

        self.update_student_id_text = StringVar(value=student_info[1])
        self.update_student_name_text = StringVar(value=student_info[2])
        self.update_student_surname_text = StringVar(value=student_info[3])
        self.update_student_dob_text = StringVar(value=student_info[4])
        self.update_gender_selected = StringVar(value=student_info[5])
        self.update_student_address_text = StringVar(value=student_info[6])
        self.update_student_contact_num_text = StringVar(value=student_info[7])
        self.update_student_email_text = StringVar(value=student_info[8])
        self.update_res_role = StringVar(value=student_info[9])
        self.update_student_course_text = StringVar(value=student_info[10])
        self.update_student_type = StringVar(value=student_info[11])
        self.update_student_typ = StringVar(value=student_info[12])

        # Default options for radio buttons
        self.update_gender_selected.set("Female")
        self.update_res_role.set("Yes")
        self.update_student_type.set("Full-Time")
        self.update_student_typ.set("Face-Face")

        update_heading_label = Label(update_window, text="    Update Student Form", font=heading_font)
        update_heading_label.grid(row=0, column=2)

        # Adding labels and entry boxes for Student details
        update_student_id = Label(update_window, text="Student ID:", font=("Bold", 12), pady=20, padx=10)
        update_student_id.grid(row=1, column=0, sticky=W)
        self.update_student_id_entry = Entry(update_window, textvariable=self.update_student_id_text)
        self.update_student_id_entry.grid(row=1, column=1)

        update_student_name = Label(update_window, text="Student Name:", font=("Bold", 12), pady=10, padx=10)
        update_student_name.grid(row=1, column=4, sticky=W)
        self.update_student_name_entry = Entry(update_window, textvariable=self.update_student_name_text, )
        self.update_student_name_entry.grid(row=1, column=5)

        update_student_surname = Label(update_window, text="Student Surname: ", font=("Bold", 12), pady=10, padx=10)
        update_student_surname.grid(row=2, column=0, sticky=W)
        self.update_student_surname_entry = Entry(update_window, textvariable=self.update_student_surname_text, )
        self.update_student_surname_entry.grid(row=2, column=1)

        update_student_dob = Label(update_window, text="Date of Birth:", font=("Bold", 12), pady=10, padx=10)
        update_student_dob.grid(row=2, column=4, sticky=W)
        self.update_student_dob_entry = Entry(update_window, textvariable=self.update_student_dob_text, )
        self.update_student_dob_entry.grid(row=2, column=5)

        update_student_contact = Label(update_window, text="Contact: ", font=("Bold", 12), pady=10, padx=10)
        update_student_contact.grid(row=3, column=0, sticky=W)
        self.update_student_contact_entry = Entry(update_window, textvariable=self.update_student_contact_num_text, )
        self.update_student_contact_entry.grid(row=3, column=1)

        update_student_address = Label(update_window, text="Address: ", font=("Bold", 12), pady=10, padx=10)
        update_student_address.grid(row=3, column=4, sticky=W)
        self.update_student_address_entry = Entry(update_window, textvariable=self.update_student_address_text, )
        self.update_student_address_entry.grid(row=3, column=5)

        update_student_gender_label = Label(update_window, text="Gender", font=("Bold", 12), pady=10, padx=10)
        update_student_gender_label.grid(row=4, column=0, sticky=W)
        update_student_female_radio = Radiobutton(update_window, text="Female", variable=self.update_gender_selected, value="Female")
        update_student_female_radio.grid(row=4, column=1)
        update_student_male_radio = Radiobutton(update_window, text="Male", variable=self.update_gender_selected, value="Male")
        update_student_male_radio.grid(row=5, column=1)

        update_student_res = Label(update_window, text="Resident Student ", font=("Bold", 12), pady=10, padx=10)
        update_student_res.grid(row=4, column=4, sticky=W)
        update_yes_radio = Radiobutton(update_window, text="Yes", variable=self.update_res_role, value="Yes")
        update_yes_radio.grid(row=4, column=5)
        update_no_radio = Radiobutton(update_window, text="No", variable=self.update_res_role, value="No")
        update_no_radio.grid(row=5, column=5)

        update_student_email = Label(update_window, text="Email Address: ", font=("Bold", 12), pady=10, padx=10)
        update_student_email.grid(row=6, column=0, sticky=W)
        self.update_student_email_entry = Entry(update_window, textvariable=self.update_student_email_text)
        self.update_student_email_entry.grid(row=6, column=1)

        update_student_course = Label(update_window, text="Course:", font=("Bold", 12), pady=10, padx=10)
        update_student_course.grid(row=6, column=4, sticky=W)
        self.update_student_course_entry = Entry(update_window, textvariable=self.update_student_course_text, )
        self.update_student_course_entry.grid(row=6, column=5)

        update_student_type = Label(update_window, text="Type ", font=("Bold", 12), pady=10, padx=10)
        update_student_type.grid(row=7, column=0, sticky=W)
        update_full_radio = Radiobutton(update_window, text="Full-Time", variable=self.update_student_type, value="Full-Time", pady=10)
        update_full_radio.grid(row=7, column=1)
        update_part_radio = Radiobutton(update_window, text="Part-Time", variable=self.update_student_type, value="Part-Time", pady=10)
        update_part_radio.grid(row=8, column=1)

        update_mode_label = Label(update_window, text="Learning Mode", font=("Bold", 12), pady=10, padx=10)
        update_mode_label.grid(row=7, column=4, sticky=W)
        update_face_radio = Radiobutton(update_window, text="Face-Face", variable=self.update_student_typ, value="Face-Face")
        update_face_radio.grid(row=7, column=5)
        update_online_radio = Radiobutton(update_window, text="Online", variable=self.update_student_typ, value="Online")
        update_online_radio.grid(row=8, column=5)

        # Buttons to submit the student details and to navigate to the crud window
        update_btn = Button(update_window, text="Update", width=10, bg="#90E0EF", fg="black", font= button_font2, command=lambda: self.update_student_details(student_info[0]))
        update_btn.grid(row=10, column=2)

        update_back_btn = Button(update_window, text="Back", width=10,bg="#90E0EF", fg="black", font= button_font2, command=self.open_crud_window)
        update_back_btn.grid(row=10, column=3)

    # Function to open a window for deleting a student
    def delete_student_window(self):
        if self.current_window:
            self.current_window.withdraw()

        delete_window = Toplevel(self.master)
        delete_window.geometry("700x465")
        delete_window.title("Delete Details ")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        delete_heading = Label(delete_window, text="    Select a Student to Delete", font=heading_font)
        delete_heading.pack()

        self.current_window = delete_window

        # Treeview to display the student details
        self.student_list = ttk.Treeview(delete_window, columns=("No",
                                                                   "StudentId",
                                                                   "Name", "Surname",
                                                                   "DOB", "Gender",
                                                                   "Address", "Contact",
                                                                   "Email", "Resident",
                                                                   "Course", "Student Type",
                                                                   "Learning Mode"), show='headings', height=15)


        for col in self.student_list["columns"]:
            self.student_list.heading(col, text=col)
            self.student_list.column(col, width=100, anchor='center')
        self.student_list.pack(pady=10)

        Populate().populate_student_list(self)

        delete_btn = Button(delete_window, text="Delete", width=10, bg="#90E0EF", fg="black", font= button_font2, command=self.delete_selected_student)
        delete_btn.pack(pady=10)
        delete_back_btn = Button(delete_window, text="Back", width=10, bg="#90E0EF", fg="black", font= button_font2,command=self.open_crud_window)
        delete_back_btn.pack()

    # Function to open a window for adding a Lecturer
    def create_lecturer_window(self):
        if self.current_window:
            self.current_window.withdraw()

        lecturer_window = Toplevel(self.master)
        lecturer_window.geometry("860x400")
        lecturer_window.title("Lecturer Details")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = lecturer_window

        self.lec_id_text = StringVar()
        self.lecturer_name_text = StringVar()
        self.lecturer_surname_text = StringVar()
        self.lecturer_specialisation_text = StringVar()
        self.lecturer_course_text = StringVar()
        self.lecturer_gender = StringVar()
        self.lecturer_address_text = StringVar()
        self.lecturer_email_text = StringVar()
        self.lecturer_title_text = StringVar()
        self.lecturer_qual_text = StringVar()
        self.lecturer_contact_text = StringVar()

        self.lecturer_gender.set("Female")

        lec_heading_label = Label(lecturer_window, text="Lecturer Registration Form", font=heading_font)
        lec_heading_label.grid(row=0, column=2)

        # Adding labels and entry boxes for Lecturer details
        lecturer_title = Label(lecturer_window, text="Title: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_title.grid(row=1, column=0, sticky=W)
        self.lecturer_title_entry = Entry(lecturer_window, textvariable=self.lecturer_title_text, )
        self.lecturer_title_entry.grid(row=1, column=1)

        lec_id = Label(lecturer_window, text="Lecturer ID: ", font=("Bold", 12), pady=10, padx=10)
        lec_id.grid(row=1, column=4, sticky=W)
        self.lec_id_entry = Entry(lecturer_window, textvariable=self.lec_id_text, )
        self.lec_id_entry.grid(row=1, column=5)

        lecturer_name = Label(lecturer_window, text="Lecturer Name: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_name.grid(row=2, column=0, sticky=W)
        self.lecturer_name_entry = Entry(lecturer_window, textvariable=self.lecturer_name_text, )
        self.lecturer_name_entry.grid(row=2, column=1)

        lecturer_surname = Label(lecturer_window, text="Lecturer Surname: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_surname.grid(row=2, column=4, sticky=W)
        self.lecturer_surname_entry = Entry(lecturer_window, textvariable=self.lecturer_surname_text, )
        self.lecturer_surname_entry.grid(row=2, column=5)

        lecturer_gender_label = Label(lecturer_window, text="Gender:", font=("Bold", 12), pady=10, padx=10)
        lecturer_gender_label.grid(row=3, column=0, sticky=W)
        lec_female_radio = Radiobutton(lecturer_window, text="Female", variable=self.lecturer_gender, value="Female")
        lec_female_radio.grid(row=3, column=1)
        lec_male_radio = Radiobutton(lecturer_window, text="Male", variable=self.lecturer_gender, value="Male")
        lec_male_radio.grid(row=4, column=1)

        lecturer_contact = Label(lecturer_window, text="Contact Number: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_contact.grid(row=3, column=4, sticky=W)
        self.lecturer_contact_entry = Entry(lecturer_window, textvariable=self.lecturer_contact_text, )
        self.lecturer_contact_entry.grid(row=3, column=5)

        lecturer_email_label = Label(lecturer_window, text="Email Address:", font=("Bold", 12), pady=10, padx=10)
        lecturer_email_label.grid(row=5, column=0, sticky=W)
        self.lecturer_email_entry = Entry(lecturer_window, textvariable=self.lecturer_email_text, )
        self.lecturer_email_entry.grid(row=5, column=1)

        lecturer_address_label = Label(lecturer_window, text="Address: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_address_label.grid(row=5, column=4, sticky=W)
        self.lecturer_address_entry = Entry(lecturer_window, textvariable=self.lecturer_address_text)
        self.lecturer_address_entry.grid(row=5, column=5)

        lecturer_qual = Label(lecturer_window, text="Qualifications: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_qual.grid(row=6, column=0, sticky=W)
        self.lecturer_qual_entry = Entry(lecturer_window, textvariable=self.lecturer_qual_text)
        self.lecturer_qual_entry.grid(row=6, column=1)

        lecturer_specialisation_label = Label(lecturer_window, text="Specialisation: ", font=("Bold", 12), pady=10,padx=10)
        lecturer_specialisation_label.grid(row=6, column=4, sticky=W)
        self.lecturer_specialisation_entry = Entry(lecturer_window, textvariable=self.lecturer_specialisation_text, )
        self.lecturer_specialisation_entry.grid(row=6, column=5)

        lecturer_course = Label(lecturer_window, text="Modules Taught: ", font=("Bold", 12), pady=10, padx=10)
        lecturer_course.grid(row=7, column=0, sticky=W)
        self.lecturer_course_entry = Entry(lecturer_window, textvariable=self.lecturer_course_text, )
        self.lecturer_course_entry.grid(row=7, column=1, sticky=W)

        # Button to submit the lecturer details
        lecturer_submit_btn = Button(lecturer_window, text="Add", width=10, bg="#90E0EF", fg="black", font= button_font2, command=self.add_lec)
        lecturer_submit_btn.grid(row=8, column=2)

        lec_back_btn = Button(lecturer_window, text="Back", width=10, bg="#90E0EF", fg="black", font= button_font2, command=self.open_crud_window)
        lec_back_btn.grid(row=8, column=3)

    # Function to open a window for reading Lecturer details
    def read_lecturer_window(self):
        if self.current_window:
            self.current_window.withdraw()

        if self.lecturer_list.winfo_ismapped():  # Checks if it is already displayed data in the Treeview
            return

        lecturer_read_window = Toplevel(self.master)
        lecturer_read_window.geometry("700x450")
        lecturer_read_window.title("Read Details")

        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = lecturer_read_window

        # Treeview to display the student details
        self.lecturer_list = ttk.Treeview(lecturer_read_window, columns=("No",
                                                                         "LecturerId","Title",
                                                                         "Name", "Surname",
                                                                         "Gender","Address",
                                                                         "Contact","Email",
                                                                         "Qualifications", "Specialisation",
                                                                         "ModulesTaught"), show='headings', height=15)

        for col in self.lecturer_list["columns"]:
            self.lecturer_list.heading(col, text=col)
            self.lecturer_list.column(col, width=100, anchor='center')
        self.lecturer_list.pack(pady=10)

        # Buttons to read the lecturer details and to navigate back to the crud window
        read_lec_btn = Button(lecturer_read_window, text="View", bg="#90E0EF", fg="black", font= button_font2 , width=10, command=self.pop_lecturer_list)
        read_lec_btn.pack(pady=10)
        back_lec_btn = Button(lecturer_read_window, text="Back", bg="#90E0EF", fg="black", font= button_font2, width=10, command=self.open_crud_window)
        back_lec_btn.pack(pady=10)

    # Function to open a window for updating lecturer details
    def update_lecturer_window(self, lecturer_info):
        if self.current_window:
            self.current_window.withdraw()

        update_lec_window = Toplevel(self.master)
        update_lec_window.geometry("860x400")
        update_lec_window.title("Lecturer Update Details")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = update_lec_window

        self.update_id_text = StringVar(value=lecturer_info[1])
        self.update_name_text = StringVar(value=lecturer_info[3])
        self.update_surname_text = StringVar(value=lecturer_info[4])
        self.update_specialisation_text = StringVar(value=lecturer_info[10])
        self.update_course_text = StringVar(value=lecturer_info[11])
        self.update_gender = StringVar(value=lecturer_info[5])
        self.update_address_text = StringVar(value=lecturer_info[6])
        self.update_email_text = StringVar(value=lecturer_info[8])
        self.update_title_text = StringVar(value=lecturer_info[2])
        self.update_qual_text = StringVar(value=lecturer_info[9])
        self.update_contact_text = StringVar(value=lecturer_info[7])

        self.update_gender.set("Female")

        lec_heading_label = Label( update_lec_window, text="  Lecturer Update Form", font=heading_font)
        lec_heading_label.grid(row=0, column=2)

        # Adding labels and entry boxes for Lecturer details
        update_lecturer_title = Label( update_lec_window, text="Title: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_title.grid(row=1, column=0, sticky=W)
        self.update_lecturer_title_entry = Entry( update_lec_window, textvariable=self.update_title_text, )
        self.update_lecturer_title_entry.grid(row=1, column=1)

        update_lec_id = Label( update_lec_window, text="Lecturer ID: ", font=("Bold", 12), pady=10, padx=10)
        update_lec_id.grid(row=1, column=4, sticky=W)
        self.update_lec_id_entry = Entry( update_lec_window, textvariable=self.update_id_text, )
        self.update_lec_id_entry.grid(row=1, column=5)

        update_lecturer_name = Label( update_lec_window, text="Lecturer Name: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_name.grid(row=2, column=0, sticky=W)
        self.update_lecturer_name_entry = Entry( update_lec_window, textvariable=self.update_name_text, )
        self.update_lecturer_name_entry.grid(row=2, column=1)

        update_lecturer_surname = Label( update_lec_window, text="Lecturer Surname: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_surname.grid(row=2, column=4, sticky=W)
        self.update_lecturer_surname_entry = Entry( update_lec_window, textvariable=self.update_surname_text, )
        self.update_lecturer_surname_entry.grid(row=2, column=5)

        update_lecturer_gender_label = Label( update_lec_window, text="Gender:", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_gender_label.grid(row=3, column=0, sticky=W)
        update_lec_female_radio = Radiobutton( update_lec_window, text="Female", variable=self.update_gender, value="Female")
        update_lec_female_radio.grid(row=3, column=1)
        update_lec_male_radio = Radiobutton( update_lec_window, text="Male", variable=self.update_gender, value="Male")
        update_lec_male_radio.grid(row=4, column=1)

        update_lecturer_contact = Label( update_lec_window, text="Contact Number: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_contact.grid(row=3, column=4, sticky=W)
        self.update_lecturer_contact_entry = Entry( update_lec_window, textvariable=self.update_contact_text, )
        self.update_lecturer_contact_entry.grid(row=3, column=5)

        update_lecturer_email_label = Label( update_lec_window, text="Email Address:", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_email_label.grid(row=5, column=0, sticky=W)
        self.update_lecturer_email_entry = Entry( update_lec_window, textvariable=self.update_email_text, )
        self.update_lecturer_email_entry.grid(row=5, column=1)

        update_lecturer_address_label = Label( update_lec_window, text="Address: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_address_label.grid(row=5, column=4, sticky=W)
        self.update_lecturer_address_entry = Entry( update_lec_window, textvariable=self.update_address_text)
        self.update_lecturer_address_entry.grid(row=5, column=5)

        update_lecturer_qual = Label( update_lec_window, text="Qualifications: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_qual.grid(row=6, column=0, sticky=W)
        self.update_lecturer_qual_entry = Entry( update_lec_window, textvariable=self.update_qual_text)
        self.update_lecturer_qual_entry.grid(row=6, column=1)

        update_lecturer_specialisation_label = Label( update_lec_window, text="Specialisation: ", font=("Bold", 12), pady=10,
                                              padx=10)
        update_lecturer_specialisation_label.grid(row=6, column=4, sticky=W)
        self.update_lecturer_specialisation_entry = Entry( update_lec_window, textvariable=self.update_specialisation_text, )
        self.update_lecturer_specialisation_entry.grid(row=6, column=5)

        update_lecturer_course = Label( update_lec_window, text="Modules Taught: ", font=("Bold", 12), pady=10, padx=10)
        update_lecturer_course.grid(row=7, column=0, sticky=W)
        self.update_lecturer_course_entry = Entry( update_lec_window, textvariable=self.update_course_text, )
        self.update_lecturer_course_entry.grid(row=7, column=1, sticky=W)

        # Button to submit the lecturer details
        lecturer_update_btn = Button( update_lec_window, text="Update", bg="#90E0EF", fg="black", font= button_font2 , width=10, command= lambda: self.update_lecturer_details(lecturer_info[0]))
        lecturer_update_btn.grid(row=8, column=2)

        update_lec_back_btn = Button( update_lec_window, text="Back", bg="#90E0EF", fg="black", font= button_font2, width=10, command=self.open_crud_window)
        update_lec_back_btn.grid(row=8, column=3)

    # Function to open a window for deleting a Lecturer
    def delete_lecturer_window(self):
        if self.current_window:
            self.current_window.withdraw()

        lecturer_delete_window = Toplevel(self.master)
        lecturer_delete_window.geometry("700x500")
        lecturer_delete_window.title("Delete Details")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        delete_heading = Label(lecturer_delete_window, text="Select a Lecturer to Delete", font=heading_font)
        delete_heading.pack()

        self.current_window = lecturer_delete_window

        self.lecturer_list = ttk.Treeview(lecturer_delete_window, columns=("No",
                                                                         "LecturerId", "Title",
                                                                         "Name", "Surname",
                                                                         "Gender", "Address",
                                                                         "Contact", "Email",
                                                                         "Qualifications", "Specialisation",
                                                                         "ModulesTaught"), show='headings', height=15)

        for col in self.lecturer_list["columns"]:
            self.lecturer_list.heading(col, text=col)
            self.lecturer_list.column(col, width=100, anchor='center')
        self.lecturer_list.pack(pady=10)

        Populate().populate_lecturer_list(self)

        # Button to read the lecturer details
        delete_lec_btn = Button(lecturer_delete_window, text="Delete", width=10, bg="#90E0EF", fg="black", font= button_font2, command=self.delete_selected_lecturer)
        delete_lec_btn.pack(pady=10)

        back_lec_btn = Button(lecturer_delete_window, text="Back",  width=10, bg="#90E0EF", fg="black", font= button_font2, command=self.open_crud_window)
        back_lec_btn.pack(pady=10)

    # Function to choose which student to Update
    def open_student_selection_window(self):
        if self.current_window:
            self.current_window.withdraw()

        selection_window = Toplevel(self.master)
        selection_window.geometry("700x430")
        selection_window.title("Select to Edit")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = selection_window

        selection_heading = Label(selection_window, text=" Select a Student to Edit", font=heading_font)
        selection_heading.pack()

        self.student_list = ttk.Treeview(selection_window, columns=("No",
                                                               "StudentId",
                                                               "Name", "Surname",
                                                               "DOB", "Gender",
                                                               "Address", "Contact",
                                                               "Email", "Resident",
                                                               "Course", "Student Type",
                                                               "Learning Mode"), show='headings', height=15)
        for col in self.student_list["columns"]:
            self.student_list.heading(col, text=col)
            self.student_list.column(col, width=100, anchor='center')
        self.student_list.pack(pady=10)

        student_edit_btn = Button(selection_window, text="Edit", width=10,bg="#90E0EF", fg="black", font= button_font2, command=self.open_student_edit_window)
        student_edit_btn.pack(pady=10)

        Populate().populate_student_list(self)

    # Function sends the selected student's data to update_student_window to be edited
    def open_student_edit_window(self):
        # Gets the selected student
        selected_item = self.student_list.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student to edit.")
            return

        # Gets the selected student's data
        student_data = self.student_list.item(selected_item[0])["values"]

        # Passes the selected student's data to the edit window
        self.update_student_window(student_data)

    # Function to choose which lecturer to Update
    def open_lecturer_selection_window(self):
        if self.current_window:
            self.current_window.withdraw()

        selection_window = Toplevel(self.master)
        selection_window.geometry("700x430")
        selection_window.title("Select to Edit")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = selection_window

        selection_heading = Label(selection_window, text="    Select a Lecturer to Edit", font=heading_font)
        selection_heading.pack()

        self.lecturer_list = ttk.Treeview(selection_window, columns=("No",
                                                                         "LecturerId", "Title",
                                                                         "Name", "Surname",
                                                                         "Gender", "Address",
                                                                         "Contact", "Email",
                                                                         "Qualifications", "Specialisation",
                                                                         "ModulesTaught"), show='headings', height=15)
        for col in self.lecturer_list["columns"]:
            self.lecturer_list.heading(col, text=col)
            self.lecturer_list.column(col, width=100, anchor='center')
        self.lecturer_list.pack(pady=10)

        # Button to read the lecturer details
        update_edit_btn = Button(selection_window, text="Edit", bg="#90E0EF", fg="black", font= button_font2, width=10,command=self.open_lecturer_edit_window)
        update_edit_btn.pack(pady=10)

        Populate().populate_lecturer_list(self)

    # Function sends the selected lecturer's data to update_lecturer_window to be edited
    def open_lecturer_edit_window(self):
        # Get the selected Lecturer
        selected_item = self.lecturer_list.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a Lecturer to edit.")
            return

        # fetch the selected lecturer's data
        lecturer_data = self.lecturer_list.item(selected_item[0])["values"]

        # Pass the selected lecturer's data to the edit window
        self.update_lecturer_window(lecturer_data)

    # Function to choose which student to delete
    def delete_selected_student(self):
        # Get the selected student
        selected_item = self.student_list.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student to delete.")
            return

        # Get the selected student's ID
        StudentId = self.student_list.item(selected_item[0])["values"][1]
        Delete().delete_student(self, StudentId)

    # Function to choose which lecturer to delete
    def delete_selected_lecturer(self):
        # Get the selected student
        selected_item = self.lecturer_list.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a lecturer to delete.")
            return

        # Get the selected student's ID
        LecturerId = self.lecturer_list.item(selected_item[0])["values"][1]
        Delete().delete_lecturer(self, LecturerId)

    # Function to search for a student
    def search_student_window(self):
        if self.current_window:
            self.current_window.withdraw()

        search_window = Toplevel(self.master)
        search_window.geometry("700x500")
        search_window.title("Search")

        heading_font = font.Font(family="Helvetica", size=12, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = search_window

        self.search_term = StringVar()

        search_label = Label(search_window, text="Enter Name or Student ID:", font=heading_font)
        search_label.pack(pady=10)
        search_entry = Entry(search_window, textvariable=self.search_term, width=30)
        search_entry.pack()

        self.search_results_student = ttk.Treeview(search_window, columns=("No",
                                                               "StudentId",
                                                               "Name", "Surname",
                                                               "DOB", "Gender",
                                                               "Address", "Contact",
                                                               "Email", "Resident",
                                                               "Course", "Student Type",
                                                               "Learning Mode"), show='headings', height=15)

        for col in self.search_results_student["columns"]:
            self.search_results_student.heading(col, text=col)
            self.search_results_student.column(col, width=100, anchor='center')

        self.search_results_student.pack(pady=10)

        # Search button that triggers the search_student function
        search_button = Button(search_window, text="Search", width= 10, bg="#90E0EF", fg="black", font= button_font2, command= self.perform_student_search)
        search_button.pack(pady=10)

        back_button = Button(search_window, text="Back", width=10, bg="#90E0EF", fg="black", font= button_font2,command=self.open_crud_window)
        back_button.pack(pady=10)

    # This function gets the text in the textbox and then calls the search_student function in the Search class and checks for matching student details.
    def perform_student_search(self):
        search_term = self.search_term.get()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter an ID OR Name.")
            return

        Search().search_student(self, search_term)

    # Function to search for a lecturer
    def search_lecturer_window(self):
        if self.current_window:
            self.current_window.withdraw()

        search_lecturer_window = Toplevel(self.master)
        search_lecturer_window.geometry("700x500")
        search_lecturer_window.title("Search")

        heading_font = font.Font(family="Helvetica", size=15, weight="bold")
        button_font2 = font.Font(family="Helvetica", size=10, weight="bold")

        self.current_window = search_lecturer_window

        self.search_lecturer_term = StringVar()

        search_lecturer_label = Label(search_lecturer_window, text="Enter Name or Lecturer ID:", font=heading_font)
        search_lecturer_label.pack(pady=10)
        search_lecturer_entry = Entry(search_lecturer_window, textvariable=self.search_lecturer_term, width=30)
        search_lecturer_entry.pack()

        self.search_results_lecturer = ttk.Treeview(search_lecturer_window, columns=("No",
                                                                         "LecturerId", "Title",
                                                                         "Name", "Surname",
                                                                         "Gender", "Address",
                                                                         "Contact", "Email",
                                                                         "Qualifications", "Specialisation",
                                                                         "ModulesTaught"), show='headings', height=15)

        for col in self.search_results_lecturer["columns"]:
            self.search_results_lecturer.heading(col, text=col)
            self.search_results_lecturer.column(col, width=100, anchor='center')

        self.search_results_lecturer.pack(pady=10)

        search_lecturer_button = Button(search_lecturer_window, text="Search", width=10,bg="#90E0EF", fg="black", font= button_font2, command=self.perform_lecturer_search)
        search_lecturer_button.pack(pady=10)
        back_button = Button(search_lecturer_window, text="Back", width=10, bg="#90E0EF", fg="black", font= button_font2,command=self.open_crud_window)
        back_button.pack(pady=10)

    #This function gets the text in the textbox and then calls the search_lecturer function in the Search class and checks for matching lecturer details.
    def perform_lecturer_search(self):
        search_term = self.search_lecturer_term.get()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter an ID OR Name.")
            return

        Search().search_lecturer(self, search_term)

    # Methods for clearing textboxes
    def clear_create_student(self):
        self.student_id_text.set("")
        #self.student_id_text.delete()
        self.student_name_text.set("")
        self.student_surname_text.set("")
        self.student_dob_text.set("")
        self.gender_selected.set("")
        self.student_address_text.set("")
        self.student_contact_num_text.set("")
        self.student_email_text.set("")
        self.res_role.set("")
        self.student_course_text.set("")
        self.student_type.set("")
        self.student_typ.set("")

    def clear_create_lecturer(self):
        self.lec_id_text.set("")
        self.lecturer_name_text.set("")
        self.lecturer_surname_text.set("")
        self.lecturer_specialisation_text.set("")
        self.lecturer_course_text.set("")
        self.lecturer_gender.set("")
        self.lecturer_address_text.set("")
        self.lecturer_email_text.set("")
        self.lecturer_title_text.set("")
        self.lecturer_qual_text.set("")
        self.lecturer_contact_text.set("")

    # Function to show the select role window(main window)
    def show_main_window(self):
        if self.current_window:
            self.current_window.destroy()
        self.master.deiconify()
        self.current_window = None

    # Function to set the background color of windows
    def set_background_color(self,color):
        self.master.configure(bg="#03045E")
        #color

    # Instantiating the methods from Add, Populate, Update, Delete class
    def add_stu(self):
        Add().add_student(self)

    def add_lec(self):
        Add().add_lecturer(self)

    def pop_student_list(self):
        Populate().populate_student_list(self)

    def pop_lecturer_list(self):
        Populate().populate_lecturer_list(self)

    def update_student_details(self, no):
        Update().update_student(self,no)

    def update_lecturer_details(self, no):
        Update().update_lecturer(self,no)

    def delete_student_list(self, StudentId):
        Delete().delete_student(self, StudentId)

    def delete_lecturer_list(self, LecturerId):
        Delete().delete_lecturer(self, LecturerId)
