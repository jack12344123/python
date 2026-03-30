name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
domestic_student = str(input("are you a student:(yes/no) "))
annual_family = float(input("Enter your annual family: "))
if domestic_student == "yes":
    if gpa >= 8.5 and (annual_family< 40000):
        print("congratulations")
    else: print ("to bad")


