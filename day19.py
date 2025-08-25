# message="I am global"
# def show_message():
#     message="I am local"
#     print(message)
# show_message()    
# print(message)    


                    # Write recursive factorial and Fibonacci functions

# def Factorial(n):
#     if n==0 or n==1:
#         return 1    
#     else:
#         return n*Factorial(n-1)  
# n=int(input("Enter a number="))         
# x=Factorial(n)
# print(x)         

def  Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  Fibonacci(n-1) +  Fibonacci(n-2)

n=int(input("Enter a number=")) 
x=Fibonacci(n)
print(x)         