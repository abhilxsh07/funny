import mysql.connector as m

# Establish connection to the database
con = m.connect(host='localhost', user='root', password='root', database='test_env')
cur = con.cursor()

# Create student table if it doesn't exist
t = '''
    CREATE TABLE IF NOT EXISTS student (
        Admission_Number INT PRIMARY KEY,
        Name VARCHAR(25),
        Class INT,
        Section CHAR(1),
        Stream VARCHAR(10),
        Date_of_birth DATE,
        Gender CHAR(1),
        Blood_Group VARCHAR(5),
        Religion VARCHAR(10),
        Contact_Number VARCHAR(13)
    )
'''
cur.execute(t)
con.commit()

# Functions for managing student records

def gender():
    cur.execute("SELECT gender, COUNT(*) FROM student GROUP BY gender")
    students = cur.fetchall()
    print("Gender \t Count")
    for gender, count in students:
        print(gender, "\t", count)

def section():
    cur.execute("SELECT Class, Section, COUNT(*) FROM student GROUP BY Class, Section")
    students = cur.fetchall()
    print("Class \t Section \t Count")
    for cls, section, count in students:
        print(cls, "\t", section, "\t\t", count)

def stream():
    cur.execute("SELECT stream, COUNT(*) FROM student GROUP BY stream")
    students = cur.fetchall()
    print("Stream \t\t Count")
    for stream, count in students:
        print(stream, '\t', count)

def religion():
    cur.execute("SELECT religion, COUNT(*) FROM student GROUP BY religion")
    students = cur.fetchall()
    print("Religion \t Count")
    for religion, count in students:
        print(religion, '\t\t', count)

def names():
    cur.execute("SELECT * FROM student ORDER BY name")
    students = cur.fetchall()
    print("Admission no \t Name \t\t Class \t Section \t Stream \t DOB \t\t Gender \t Blood Group \t Religion \t Contact no.")
    for student in students:
        print(student[0], "\t\t", student[1], "\t", student[2], "\t", student[3], "\t\t", student[4], "\t", student[5], "\t", student[6], "\t\t", student[7], "\t\t", student[8], "\t\t", student[9])

def update():
    Admn = int(input("Enter the Admission no. of the student whose details are to be updated: "))
    try:
        cur.execute("SELECT * FROM student WHERE Admission_Number = %s", (Admn,))
        students = cur.fetchall()
        
        if not students:
            print("No student found with Admission number", Admn)
            return
        
        print("Admission no \t Name \t\t Class \t Section \t Stream \t DOB \t\t Gender \t Blood Group \t Religion \t Contact no.")
        
        for student in students:
            print(student[0], "\t\t", student[1], "\t", student[2], "\t", student[3], "\t\t", student[4], "\t", student[5], "\t", student[6], "\t\t", student[7], "\t\t", student[8], "\t\t", student[9])
        
        columns = {
            1: "Admission_Number",
            2: "Name",
            3: "Class",
            4: "Section",
            5: "Stream",
            6: "Date_of_birth",
            7: "Gender",
            8: "Blood_Group",
            9: "Religion",
            10: "Contact_Number"
        }

        change = int(input("Enter index number of column to be changed (1-10): "))
        
        if change not in columns:
            print("Invalid index")
            return
        
        new_value = input("Enter the new value for " + columns[change] + ": ")

        query = "UPDATE student SET " + columns[change] + " = %s WHERE Admission_Number = %s"
        cur.execute(query, (new_value, Admn))
        
        print("Updated", columns[change], "for student with Admission number", Admn)
    
    except Exception as e:
        print("Error:", e)

    con.commit()

def yeet():
    try:
        Admn = int(input("Enter the Admission no. of the student whose record is to be deleted: "))
        cur.execute("SELECT * FROM student WHERE Admission_Number = %s", (Admn,))
        student = cur.fetchone()
        
        if not student:
            print("No student found with Admission number", Admn)
            return
        
        query = "DELETE FROM student WHERE Admission_Number = %s"
        cur.execute(query, (Admn,))
        con.commit()
        print("Record deleted successfully!")
    
    except Exception as e:
        print("Error:", e)

def add():
    try:
        Admn = int(input("Enter the Admission number: "))
        Name = input("Enter the Name: ")
        Class = int(input("Enter the Class: "))
        Section = input("Enter the Section: ")
        Stream = input("Enter the Stream: ")
        Date_of_birth = input("Enter the Date of Birth (YYYY-MM-DD): ")
        Gender = input("Enter the Gender (M/F): ")
        Blood_Group = input("Enter the Blood Group: ")
        Religion = input("Enter the Religion: ")
        Contact_Number = input("Enter the Contact number: ")

        if len(Contact_Number) > 13:
            print("Contact number is too long! Please ensure it is within 13 characters.")
            return

        query = """
            INSERT INTO student (Admission_Number, Name, Class, Section, Stream, Date_of_birth, Gender, Blood_Group, Religion, Contact_Number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        cur.execute(query, (Admn, Name, Class, Section, Stream, Date_of_birth, Gender, Blood_Group, Religion, Contact_Number))
        con.commit()

        print("New student added successfully!")

    except Exception as e:
        print("Error:", e)

def lookup():
    try:
        name = input("Enter the name of the student: ")
        query = "SELECT * FROM student WHERE Name = %s"
        cur.execute(query, (name,))
        students = cur.fetchall()

        if students:
            print("Admission no \t Name \t\t Class \t Section \t Stream \t DOB \t\t Gender \t Blood Group \t Religion \t Contact no.")
            for student in students:
                print(student[0], "\t\t", student[1], "\t", student[2], "\t", student[3], "\t\t", student[4], "\t", student[5], "\t", student[6], "\t\t", student[7], "\t\t", student[8], "\t\t", student[9])
        else:
            print("No student found with the name", name)
    
    except Exception as e:
        print("Error:", e)

def show_students_in_section():
    section = input("Enter the section: ")
    cur.execute("SELECT * FROM student WHERE Section = %s", (section,))
    students = cur.fetchall()

    if students:
        print("Admission no \t Name \t\t Class \t Section \t Stream \t DOB \t\t Gender \t Blood Group \t Religion \t Contact no.")
        for student in students:
            print(student[0], "\t\t", student[1], "\t", student[2], "\t", student[3], "\t\t", student[4], "\t", student[5], "\t", student[6], "\t\t", student[7], "\t\t", student[8], "\t\t", student[9])
    else:
        print("No students found in section", section)

def class_lookup():
    cur.execute("SELECT DISTINCT Class FROM student")
    grades = cur.fetchall()
    print("Available Grades:")
    for grade in grades:
        print(grade[0])
    
    selected_class = int(input("Enter the grade you want to check: "))
    cur.execute("SELECT DISTINCT Section FROM student WHERE Class = %s", (selected_class,))
    sections = cur.fetchall()
    if not sections:
        print("No sections found for grade", selected_class)
        return

    print("Available Sections:")
    for section in sections:
        print(section[0])
    
    selected_section = input("Enter the section you want to check: ")
    cur.execute("SELECT * FROM student WHERE Class = %s AND Section = %s", (selected_class, selected_section))
    students = cur.fetchall()

    if students:
        print("Admission no \t Name \t\t Class \t Section \t Stream \t DOB \t\t Gender \t Blood Group \t Religion \t Contact no.")
        for student in students:
            print(student[0], "\t\t", student[1], "\t", student[2], "\t", student[3], "\t\t", student[4], "\t", student[5], "\t", student[6], "\t\t", student[7], "\t\t", student[8], "\t\t", student[9])
    else:
        print("No students found in grade", selected_class, "section", selected_section)

# Main interactive loop
while True: 
    print("""
    
    1) Show number of students of each gender
    2) Show number of students in each section
    3) Show number of students based on stream
    4) Show number of students based on religion
    5) Show details of all students in ascending order of name
    6) Update students' details
    7) Remove students from table
    8) Add a new student 
    9) Lookup a student based on name
    10) Lookup students by grade and section
    11) Leave the console
    """)

    choice = int(input("Enter the choice you wish to make: "))

    if choice == 1:
        gender()

    elif choice == 2:
        section()

    elif choice == 3:
        stream()

    elif choice == 4:
        religion()

    elif choice == 5:
        names()

    elif choice == 6: 
        update()

    elif choice == 7:
        yeet()

    elif choice == 8:
        add()

    elif choice == 9:
        lookup()

    elif choice == 10:
        class_lookup()

    elif choice == 11:
        break

    else:
        print("Invalid Choice! Please enter a valid input.")

# Close cursor and connection
cur.close()
con.close()

