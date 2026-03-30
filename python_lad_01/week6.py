
def check_result(m):
    if m >= 60:
        grade = "pass"
    else:
        grade = "fail"

    return grade
marks = [55, 70, 62, 40, 90]
for mark in marks:
    print(mark,check_result(mark))







