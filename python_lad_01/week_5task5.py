student_grades = {}
while True:
    student_name = input('please enter student name: ')
    if student_name == 'stop':
        break
    marks = int(input('please enter student marks: '))
    if marks == 'stop':
        break
    student_grades[student_name] = marks
for name, mark in student_grades.items():
    if mark >= 60:
        print(name, ":", mark,"pass")
    else:
        print(name, ":", mark, "fail")
