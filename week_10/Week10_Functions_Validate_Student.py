def validate_student(name, age, email):

    if name == "":
        return False, "invalid name"
    if name.isdigit():
        return False, "invalid name"

    if not age.isdigit():
        return False, "invalid age"
    age = int(age)
    if age <= 18 or age >= 60:
        return False, "invalid age"

    if email =="":
        return False, "invalid email"
    if "@" not in email or "." not in email:
        return False, "invalid email"
    if " " in email:
        return False, "invalid email"
    return True, "valid"
#print(validate_student("jaqck"   , '44', "jackh.hh"))






