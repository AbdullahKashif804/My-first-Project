# def greet(name):
#     print("Hello!",name)
   
# greet("Abdullah")


# def square(num):
#     return num*num
# num=int(input("Enter a num="))
# x=square(num)
# print("The square of ",num,"=",x)

def convert_temperature(value,scale):
    if scale.upper() == "C":
        return f"{(value*9/5)+32:.2f} °F"
    elif scale.upper() == "F":
        return f"{(value-32)*5/9:.2f} °C"
    else:
         return("Invalid scale.Enter C or F")
value=float(input("Enter a value="))
scale=input("Enter a scale=")
Temperature=convert_temperature(value,scale) 
print("Converted_temperature=",Temperature)