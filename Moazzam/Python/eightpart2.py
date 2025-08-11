# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("ali")
# print(s1.name)        
# del s1
# print(s1.name)

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass

# acc1=Account("12345","2803")
# print(acc1.acc_no)
# print(acc1.__acc_pass)

# class person:
#     __name="ali"

#     def __hello(self):
#         print("hello user")

#     def welcome(self):
#         self.__hello()

# p1=person()
# print(p1.welcome())    

# class car:
#     color="balck"
#     @staticmethod
#     def start():
#        print("car started")

#     @staticmethod
#     def stop():
#        print("car stoped")

# class toyotacar(car):
#    def __init__(self,name):
#       self.name=name

# car1=toyotacar("fortuner")
# print(car1.color)             


# class car:
#     @staticmethod
#     def start():
#        print("car started")

#     @staticmethod
#     def stop():
#        print("car stoped")

# class toyotacar(car):
#    def __init__(self,brand):
#       self.name=brand

# class fortuner(toyotacar):
#    def __init__(self,type):
#       self.type=type       

# car1=fortuner("petrol")
# car1.start()

# class A:
#     varA="welcome to classA"
# class B:
#     varB="welcome to classB"
# class C(A,B):
#     varC="welcome to classC"
# C1=C
# print(C1.varC)
# print(C1.varB)
# print(C1.varA)


# class car:
#     def __init__(self,type):
#         self.type=type

        
#     @staticmethod
#     def start():
#        print("car started")

#     @staticmethod
#     def stop():
#        print("car stoped")

# class toyotacar(car):
#    def __init__(self,name,type):
#       self.name=name
#       super().__init__(type)

# car1=toyotacar("fortuner","petrol")
# print(car1.type)

# class person:
#     name="abdullah"

#     @classmethod
#     def changename(cls,name):
#        cls.name=name

# p1=person()
# p1.changename("ali")
# print(p1.name)        
# print(person.name)

# class student():
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def calcpercentage(self):
#       return str((self.phy+self.chem+self.math)/3)+ "%"

# stu1=student(97,96,98)
# print(stu1.calcpercentage)

# stu1.math=94
# print(stu1.calcpercentage)
    
# class complex():
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def shownumber(self):
#         print(self.real,"i+",self.img,"j")

#     def __add__(self,num2):
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return complex(newreal,newimg)

# num1=complex(2,6)
# num1.shownumber()

# num2=complex(7,4)
# num2.shownumber()

# num3=num1+num2
# num3.shownumber()    