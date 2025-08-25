                         # Prime number
# num=int(input("Enter a number="))
# if num<=1:
#     print("prime number")
# else:
#     is_prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("it is a prime number")
#     else:
#         print("it is not a prime number")            

                                 # Factorial
# num=int(input("Enter a number="))
# factorial=1
# i=1
# while i<=num:
#     factorial=factorial*i
#     i+=1
# print(factorial) 
                                  # Sum of digits   
# num=int(input("Enter a number="))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
#     print("sum of digits",sum)    
                                   # patterrn
# row=5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")    
#     print()        


# row=5
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         if i==j:
#             print("X",end=" ")
#         else:
#             print("O",end=" ")    
#     print()        

                                    # Multiplegenerator
# num=int(input("Enter a number="))
# for i in range(1,11):
#     product=num*i
#     print(num,"x",i,"=",product)
start=int(input("Enter a number="))
end=int(input("Enter a number="))                
for i in range(start,end+1):
    for j in range(1,11):
        result=i*j
        print(i,"X",j,"=",result)
