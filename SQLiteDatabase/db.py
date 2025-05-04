import sqlite3

class Database:

    def __init__(self, db): # set constructor
        self.conn = sqlite3.connect(db) # Connection object to database
        self.cur = self.conn.cursor() # cursor object to execute queries

    def insert_student(self,i, n, s, d, g, a, co, e, r, c, t, l):
        self.cur.execute("""
                         INSERT INTO Student(StudentId, StudentName, StudentSurname, Dob, Gender, Address, Contact, Email, Resident, Course, StudentType, LearningMode)
                         VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (i, n, s, d, g, a, co, e, r, c, t, l))
        self.conn.commit()

    def insert_lecturer(self,i, t, n, s, g, a, c, e, q, sp, m):
        self.cur.execute("""
                         INSERT INTO Lecturer(LecturerId, Title, LecturerName, LecturerSurname, Gender, Address, Contact, Email, Qualifications, Specialisation, ModulesTaught) 
                         VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (i, t, n, s, g, a, c, e, q, sp, m))
        self.conn.commit()

    def fetch_student(self):
        self.cur.execute("SELECT* FROM Student")
        rows= self.cur.fetchall()
        return rows

    def fetch_lecturer(self):
        self.cur.execute("SELECT * FROM Lecturer")
        rows = self.cur.fetchall()
        return rows

    def update_student(self, i, n, s, d, g, a, co, e, r, c, t, l, no):
        self.cur.execute("UPDATE Student SET "
                         "StudentID=?,"
                         "StudentName=?,"
                         "StudentSurname=?,"
                         "Dob=?,"
                         "Gender=?,"
                         "Address=?,"
                         "Contact=?,"
                         "Email=?,"
                         "Resident=?,"
                         "Course=?,"
                         "StudentType=?,"
                         "LearningMode=?"
                         "WHERE no=?",(i, n, s, d, g, a, co, e, r, c, t, l, no))
        self.conn.commit()

    def update_lecturer(self, i, t, n, s, g, a, c, e, q, sp, m, no):
        self.cur.execute("UPDATE Lecturer SET "
                         "LecturerId=?,"
                         "Title=?,"
                         "LecturerName=?,"
                         "LecturerSurname=?,"
                         "Gender=?,"
                         "Address=?,"
                         "Contact=?,"
                         "Email=?,"
                         "Qualifications=?,"
                         "Specialisation=?,"
                         "ModulesTaught=?"
                         "WHERE no=?",(i, t, n, s, g, a, c, e, q, sp, m, no))
        self.conn.commit()

    def delete_student(self,StudentId):
        self.cur.execute("DELETE FROM Student WHERE StudentId = ?", (StudentId,))
        self.conn.commit()

    def delete_lecturer(self,LecturerId):
        self.cur.execute("DELETE FROM Lecturer WHERE LecturerId = ?", (LecturerId,))
        self.conn.commit()

    def search_student(self, search_term):
        self.cur.execute("""
                         SELECT No,StudentId, StudentName, StudentSurname, Dob, Gender, Address, Contact, Email, Resident, Course, StudentType, LearningMode
                         FROM Student WHERE StudentId LIKE ? OR StudentName LIKE ? OR StudentSurname LIKE ?
                         """, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

        return self.cur.fetchall()

    def search_lecturer(self, search_term):
        self.cur.execute("""
                         SELECT No, LecturerId, Title, LecturerName, LecturerSurname, Gender, Address, Contact, Email, Qualifications, Specialisation, ModulesTaught
                         FROM Lecturer WHERE LecturerId LIKE ? OR LecturerName LIKE ? OR LecturerSurname LIKE ?
                         """, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()




"""

dbObj = Database("BelgiumCampus.db")

dbObj.insert_student("1001",
                     "Thando",
                     "Mkhize",
                     "1991-02-27",
                     "Female",
                     "45 Rose Street, Johannesburg, Gauteng",
                     "+27 82 123 4567",
                     "thando.mkhize@email.com",
                     "Yes",
                     "DipIT",
                     "Full-Time",
                     "Face-Face")

dbObj.insert_student("1002",
                     "Sipho",
                     "Ndlovu",
                     "1999-08-15",
                     "Male",
                     "23 Main Street, Durban, KwaZulu-Natal",
                     "+27 73 456 7890",
                     "sipho.ndlovu@email.com",
                     "No",
                     "BIT",
                     "Full-Time",
                     "Online")

dbObj.insert_student("1003",
                     "Zanele",
                     "Khumalo",
                     "1995-06-12",
                     "Female",
                     "12 Kings Road, Cape Town, Western Cape",
                     "+27 84 987 6543",
                     "zanele.khumalo@email.com",
                     "Yes",
                     "BCOM",
                     "Full-Time",
                     "Face-Face")

dbObj.insert_lecturer("LEC2021",
                      "Dr.",
                      "Johan",
                      "van der Merwe",
                      "Male",
                      "78 Tech Lane, Pretoria, Gauteng",
                      "+27 71 555 1234",
                      "j.vdmerwe@belgiumcampus.ac.za",
                      "PhD in Computer Science",
                      "Programming",
                      "PRG261, PRG262, PRG361, WPR261")


dbObj.insert_lecturer("LEC3032",
                      "Prof.",
                      "Nandi",
                      "Khuzwayo",
                      "Female",
                      "34 Innovation Street, Cape Town, Western Cape",
                      "+27 82 333 9876",
                      "n.khuzwayo@belgiumcampus.ac.za",
                      "MSc in Information Systems",
                      "Cybersecurity",
                      "SEC261, PET361, EHA361")


dbObj.insert_lecturer("LEC4053",
                      "Mr.",
                      "Sibusiso",
                      "Maseko",
                      "Male",
                      "101 Digital Avenue, Johannesburg, Gauteng",
                      "+27 79 444 6789",
                      "s.maseko@belgiumcampus.ac.za",
                      "BSc (Hons) in Software Engineering",
                      "Database Development",
                      "DBD261, DBD361, DBA361")

"""


"""
self.cur.execute("CREATE TABLE IF NOT EXISTS Student"
                         "(no INTEGER PRIMARY KEY AUTOINCREMENT,"
                         "StudentID TEXT,"
                         "StudentName TEXT," 
                         "StudentSurname TEXT,"
                         "Dob TEXT,"
                         "Gender TEXT,"
                         "Address TEXT,"
                         "Contact TEXT,"
                         "Email TEXT,"
                         "Resident TEXT,"
                         "Course TEXT,"
                         "StudentType TEXT,"
                         "LearningMode TEXT )")

        self.cur.execute("CREATE TABLE IF NOT EXISTS Lecturer"
                         "(no INTEGER PRIMARY KEY AUTOINCREMENT,"
                         "LecturerId TEXT,"
                         "Title TEXT,"
                         "LecturerName TEXT,"
                         "LecturerSurname TEXT,"
                         "Gender TEXT,"
                         "Address TEXT,"
                         "Contact TEXT,"
                         "Email TEXT,"
                         "Qualifications TEXT,"
                         "Specialisation TEXT,"
                         "ModulesTaught TEXT)")

        self.conn.commit()
        print("Tables Created")
"""