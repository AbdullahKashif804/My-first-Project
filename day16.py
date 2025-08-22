# Username="Abdullah804"
# Password="abd@123"
# Enter_Username=input("Enter Username=")
# Enter_Password=input("Enter Password=")
# if Enter_Usernam.lower()==Username.lower() and Enter_Password==Password:
#     print("Login Successfully")
# else:
#     print("Invalid!Try again")    
                              # Login

# Username="Abdullah804"
# Password="abd@123"

# attempts=3

# while attempts>0:
#       Enter_Username=input("Enter Username=")
#       Enter_Password=input("Enter Password=")
#       if Enter_Username.lower()==Username.lower() and Enter_Password==Password:
#             print("Login Successfully")
#             break
#       else:
#             attempts -=1
#             print("Invalid! Try again")
#             print("Remaining attempts",attempts)
# if attempts==0:
#       print("Too many attempts! Login Failed")            

                                #  Calculator
# a=int(input("Enter a first number="))
# b=int(input("Enter a second number="))

while True:
      a=int(input("Enter a first number="))
      b=int(input("Enter a second number="))
      print("Calculator")
      print("1:+(Add)")
      print("2:-(Sub)")
      print("3:*(Mul)")
      print("4:/(Div)")
      print("5:Exit")
      choice=int(input("Enter your choice="))

      if choice==1:
            print("results=",a+b)
      elif choice==2:
            print("results=",a-b)
      elif choice==3:
            print("results=",a*b)
      elif choice==4:
            if b!=0:
                  print("results=",a/b)
            else:
                  print("Math error")      
      elif choice==5:
            print("off")
            break                    
      else:
       print("Invalid choice!Try again")
      