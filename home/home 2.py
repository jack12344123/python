counter = 0
marks = [65, 72, 80, 55, 90, 68, 77,]
for marks in marks:
    if marks >= 70:
        counter = counter + 1
    print(marks, 'marks pass')
    if marks < 70:
        print(marks, 'fail')
print("Number of passes:", counter)
