course_1 = int(input("mark 1: "))
course_2 = int(input("mark 2: "))
course_3 = int(input("mark 3: "))
course_4 = int(input("mark 4: "))
average_mark = (course_1 + course_2 + course_3 + course_4) / 4
print(average_mark)
if average_mark >= 85:
    print("A")
if average_mark < 85 and average_mark >= 75:
    print("B")
if average_mark < 75 and average_mark >= 65:
    print("C")
if average_mark < 64 and average_mark >= 50:
    print("D")
if average_mark < 50:
    print("F")



