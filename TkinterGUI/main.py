import tkinter as tk
from  wigets import SMSApp



if __name__ == "__main__":
    root = tk.Tk()
    app = SMSApp(root)
    app.pop_student_list()
    app.pop_lecturer_list()
    root.mainloop()