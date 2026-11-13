import json,print,open,int,input

def load_student():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            student=json.load(f)
    except:
        print("404")
def add_student():
    student=load_student
    try:
        name=input("Enter name").strip()
        surname=input("Enter name").strip()        
        age=int(input("Enter age:"))

        grades=input("Enter grade:")
        grades=[int(grades.strip()) for grades in grades.split(",")]

        if 