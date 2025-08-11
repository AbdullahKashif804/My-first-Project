
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


while True:
    print("STUDENT REPORT CARD SYSTEM")
    print("1:Add Student")
    print("2:View Student")
    print("3:Delete Student")
    print("4:Exit")
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
        import json

        f = open("store.txt", "w")
        f.write(json.dumps(Student, indent=4))
        f.close()

        
                                #   view
    elif opinion ==2:
        std_id=input(("Enter the Studennt ID="))
        if std_id in Student:
            print(Student[std_id])
        else:
            print("Student is not in Report")
                            #  delete
    elif opinion ==3:
        std_id=input("Enter ID to delete=")
        if std_id in Student:
            del Student[std_id]
            print("Student deleted successfully")        
        else:
            print("Student not deleted")
                            #   exit  
    elif opinion==4: 
        break       
                 
    else:
        print("nothing is found")
# a=(input("Ask  for student id="))
# if a in Student:
#     print(Student[a])
# else:
#     print("Student not found")

# with open("store.txt", "w") as f:
#     json.dump(Student, f)

# with open("store.txt", "r") as f:
#     c = f.read()
#     print("store.txt")
#     print(c)
