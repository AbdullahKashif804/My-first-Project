import json
import os

# Load data from file or use default students
if os.path.exists("store.txt") and os.path.getsize("store.txt") > 0:
    try:
        with open("store.txt", "r") as f:
            Student = json.load(f)
    except json.JSONDecodeError:
        print("⚠ Data file corrupted. Starting fresh...")
        Student = {}
else:
    Student = {
        "2803": {
            "name": "Abdullah",
            "marks": {
                "Math": 98,
                "Eng": 95,
                "Urdu": 90,
            },
            "GPA": 3.7,
        },
        "2867": {
            "name": "Ali",
            "marks": {
                "Math": 58,
                "Eng": 60,
                "Urdu": 73,
            },
            "GPA": 3.1,
        },
    }

# Save data to file
def save_data():
    with open("store.txt", "w") as f:
        json.dump(Student, f, indent=4)

# Menu loop
while True:
    print("\nSTUDENT REPORT CARD SYSTEM")
    print("1: Add Student")
    print("2: View Student")
    print("3: Delete Student")
    print("4: Exit")
    
    opinion = input("Enter your choice: ")

    # Add Student
    if opinion == "1":
        student_id = input("Enter the ID: ")
        name = input("Enter the name: ")
        Math = int(input("Enter the marks of Math: "))
        Eng = int(input("Enter the marks of Eng: "))
        Urdu = int(input("Enter the marks of Urdu: "))
        
        avg = (Math + Eng + Urdu) / 3
        GPA = avg / 25
        
        Student[student_id] = {
            "name": name,
            "marks": {
                "Math": Math,
                "Eng": Eng,
                "Urdu": Urdu
            },
            "GPA": round(GPA, 2)
        }
        
        save_data()
        print("✅ New student added successfully.")

    # View Student
    elif opinion == "2":
        std_id = input("Enter the Student ID: ")
        if std_id in Student:
            print(f"\n📄 Student ID: {std_id}")
            print(f"Name: {Student[std_id]['name']}")
            print("Marks:")
            for subject, mark in Student[std_id]["marks"].items():
                print(f"  {subject}: {mark}")
            print(f"GPA: {Student[std_id]['GPA']}")
        else:
            print("❌ Student not found.")

    # Delete Student
    elif opinion == "3":
        std_id = input("Enter ID to delete: ")
        if std_id in Student:
            del Student[std_id]
            save_data()
            print("🗑 Student deleted successfully.")
        else:
            print("❌ Student not found.")

    # Exit
    elif opinion == "4":
        print("Exiting program...")
        break

    else:
        print("⚠ Invalid choice, please try again.")
