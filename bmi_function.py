def funbmi(h,w):
    bmi=w/(h*h)
    return bmi

h=float(input("Enter your height"))
w=float(input("Enter your weight"))
bmi=funbmi(h,w)
print(bmi)