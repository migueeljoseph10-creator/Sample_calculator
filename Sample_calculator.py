print("Welcome to Miguel's Calculator")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operator = input("Enter your operator:")

if operator=="+":
    print("The sum is",num1+num2)

elif operator=="-":
    print("the result is",num1-num2)

elif operator=="*":
 print("The result is",num1*num2)    

elif operator=="/":
 print("The result is ",num1/num2)

elif operator=="**":
  print(("The result is",num1**num2))

elif operator =="//":
  print("The result is ",num1//num2)

else:
 print("Invalid Operator")




