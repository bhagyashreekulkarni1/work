num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
num3=float(input("Enter third number"))
if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    if(num2>num3):
        print("num2 is greater")
    else:
        print("num3 is greater")