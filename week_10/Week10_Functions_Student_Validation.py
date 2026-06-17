from operator import truediv

from Week10_Functions_Validate_Student import *
def validate_student2():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    email = input("Please enter your email: ")
    studant, msege = validate_student(name, age, email)
    if studant == True:
        print("studanr apseted")
    else:
        print(msege)
    if name == "" or name.isdigit():
        return False, ("invalid name")
    try:
        age = int(age)
    except ValueError:
        return False, ("plz enter a number")




    if age <= 18 or age >= 60:
        return False, ("invalid age")
    if email == " " or "@" not in email or "." not in email or email.isdigit():
        return False, ("invalid email")
    return "valid"


validate_student2()
