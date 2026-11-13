import json

def load_student():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            student=json.load(f)
    except:
        print("404")