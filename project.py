print("calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

operation = int(input("Enter your choice (1-4): "))
num1=int(input("enter frist number:"))
num2=int(input("enter second number:"))
if operation==1:
    print(num1+num2)
elif operation==2:
    print(num1-num2)
elif operation==3:
    print(num1*num2)
elif operation==4:
    if num2==0:
        print("error")
    else:
        print(num1/num2)
else:
    print("Invalid operation!")