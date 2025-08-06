# class person():
#     def __init__(self,name,age,Class):
#         self.name=name
#         self.age=age
#         self.Class=Class
#     def get_info(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("class:",self.Class)
# class Teacher(person):       
#     def __init__(self, name, age, Subject):
#         super().__init__(name, age,"ICS")
#         self.subject=Subject
#     def get_info(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("Subject:",self.subject)
#         print("Class:",self.Class)
            
# p1=person("Abdullah",19,12)
# p1.get_info()  
# p2=Teacher("Abdullah",19,"Math")
# p2.get_info()

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print("name=",self.name)
        print("age=",self.age)    
class Student(person):
    def __init__(self, name, age,grade,student_id):
        super().__init__(name, age,)
        self.grade=grade
        self.student_id=student_id
    def get_info(self):
        super().get_info()
        print("grade=",self.grade)  
        print("student_id=",self.student_id)   
class Teacher(person):
    def __init__(self, name, age,subject,Teacher_id):
        super().__init__(name, age)
        self.subject=subject
        self.Teacher_id=Teacher_id
    def get_info(self):
      super().get_info() 
      print("subject=",self.subject)
      print("Teacher_id=",self.Teacher_id) 
      
s1=Student("Abdullah",19,"A+",2803)                
s2=Student("Ali",18,"A",123)
all_student=[s1,s2]
for student in all_student:
    student.get_info()
t1=Teacher("Sir Fawad",60,"Math",4587)
t2=Teacher("Sir Abdul Moiz",30,"Urdu",6790)
all_teacher=[t1,t2]
for teacher in all_teacher:
    teacher.get_info()
