assignment = float(input("Enter assignment mark (out of 100): "))
test_mark = float(input("Enter test mark (out of 100): "))
exam_mark = float(input("Enter exam mark (out of 100): "))

assignment_contribution = assignment * (30/100)
test_contribution = test_mark * (30/100)
exam_contribution = exam_mark * (40/100)

final_mark = assignment_contribution + test_contribution + exam_contribution

print(final_mark)
print(f' final mark: {final_mark:.2f} ')

if final_mark >= 80:
    print("Grade: A")
elif final_mark >= 65:
    print("Grade: B")
elif final_mark >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")