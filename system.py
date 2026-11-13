import json,print,open,int,input,any,ValueError,KeyError,TypeError,max

def load_student():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            student=json.load(f)
    except:
        print("404")

def save_student():
    try:
        with open("student.json","w",encoding="utf-8") as f:
            student=json.dump(f)
    except:
        print("404")

def addStudent():
    students = load_student()
 
    try:
        name = input("enter name: ").strip()
        surname = input("enter name: ").strip()
        ages = int(input("enter name: "))
 
        grades = input("enter grades: ")
        grades = [int(grades.strip()) for grades in grades.split(",")]
 
        if not name or not surname:
            print("name and surname cannot be empty!")
            return
 
        if age < 17:
            print("age must be greater than 17!")
            return
 
        if not grades or any(grade < 0 and grade > 100 for grade in grades):
            print("grades must be between 0 and 100!")
            return
 
        newStudent = {
            "id": max([student["id"] for student in students], default=0) + 1,
            "name": name,
            "surname": surname,
            "age": age,
            "grades": grades
        }
 
        students.append(newStudent)
 
        if save_student(students):
            print("Student added successfully!")
 
    except ValueError:
        print("please enter numeric value...")
 
    except (KeyError, TypeError) as e:
        print("Student data error:", e)

def show_student():
    print()