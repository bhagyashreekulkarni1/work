def agefunction(name, age):
    a = 100 - age
    year = str(2021 + a)
    print(name+ " you will be turned 100 years in "+year)

name = input("Enter your name")
age=int(input("Enter your age"))
agefunction(name , age)
