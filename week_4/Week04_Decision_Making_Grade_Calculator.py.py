course_1 = int(input("mark 1: "))
course_2 = int(input("mark 2: "))
course_3 = int(input("mark 3: "))
course_4 = int(input("mark 4: "))
average_mark = (course_1 + course_2 + course_3 + course_4) / 4
print(average_mark)
if course_1 >= 50 and course_2 >= 50 and course_3 >= 50 and course_4 >= 50:
    print("pass")
    if average_mark >= 85:
        print("A")
    elif average_mark >= 75:
        print("B")
    elif average_mark >= 65:
        print("C")
    elif average_mark >= 50:
        print("D")
else:
  print("f")
