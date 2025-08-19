import json
import os

if os.path.exists("store.txt"):
    with open("store.txt","r") as f:
        Student=json.load(f)
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
    "2804": {
        "name": "Ali",
        "marks": {
            "Math": 58,
            "Eng": 60,
            "Urdu": 73,
        },
        "GPA": 3.1,
    },
}
# student_id=input("Enter the id=")
# name=input("Enter the name=")
# Math=int(input("Enter the marks of Math="))
# Eng=int(input("Enter the marks of Eng="))
# Urdu=int(input("Enter the marks of Urdu="))
# avg=(Math + Eng +Urdu)/3
# GPA=avg/30

# Student[student_id]={
#     "name":name,
#     "marks":{
#         "Math":Math,
#         "Eng":Eng,
#         "Urdu":Urdu
#     },
#     "GPA":round(GPA,2)
# }
# print("New Student added")
# print(Student[student_id])
def save_data():
    with open("store.txt","w") as f:
        f.write(json.dumps(Student,indent=4))


while True:
    print("STUDENT REPORT CARD SYSTEM")
    print("1:Add Student")
    print("2:Update Student")
    print("3:View Student")
    print("4:Delete Student")
    print("5:Exit")
    opinion = int(input("Enter your opinion="))

                              # ADD
    if opinion == 1:
        student_id = input("Enter the id=")
        name = input("Enter the name=")
        Math = int(input("Enter the marks of Math="))
        Eng = int(input("Enter the marks of Eng="))
        Urdu = int(input("Enter the marks of Urdu="))
        avg = (Math + Eng + Urdu) / 3
        GPA = avg / 25

        Student[student_id] = {
              "name": name,
              "marks": {
                  "Math": Math,
                  "Eng": Eng,
                  "Urdu": Urdu
                },
                "GPA": round(GPA, 2),
       }
        print("New Student added")
        print(Student[student_id])
        
        save_data()

                               # Update
    elif opinion ==2:
        std_id=input(("Enter the student id="))
        if std_id in Student:
            print("New data",Student[std_id])

            name=input("Enter the new name(press s to keep the same):")
            Math=input("Enter the new Math(press s to keep the same):")
            Eng=input("Enter the new Eng(press s to keep the same):")
            Urdu=input("Enter the new Urdu(press s to keep the same):")

            if name.strip():
                Student[std_id]["name"]=name
            if Math.strip():
                Student[std_id]["marks"]["Math"]=int(Math)
            if Eng.strip():
                Student[std_id]["marks"]["Eng"]=int(Eng)
            if Urdu.strip():
                Student[std_id]["marks"]["Urdu"]=int(Urdu)            

            marks=Student[std_id]["marks"]    
            avg=(marks["Math"]+marks["Eng"]+marks["Urdu"])/3
            GPA=avg/25
            Student[std_id]["GPA"]=round(GPA,2)
            print("Student updated successfully")
            print(Student[std_id])


            save_data()

                                #   View
    elif opinion ==3:
        std_id=input(("Enter the Studennt ID="))
        if std_id in Student:
            print(Student[std_id])
        else:
            print("Student is not in Report")
                            #  Delete
    elif opinion ==4:
        std_id=input("Enter ID to delete=")
        if std_id in Student:
            del Student[std_id]
            print("Student deleted successfully")        
        else:
            print("Student not deleted")
                            #   Exit  
    elif opinion==5: 
        break       
                 
    else:
        print("nothing is found")
