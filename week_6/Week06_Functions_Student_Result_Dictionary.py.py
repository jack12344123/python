def print_results(dict_student):
    for mame, marks in dict_student.items():
        if marks >= 60:
            result = "pass"
            print(mame, marks, result)
        else:
            result = "fail"
            print(mame, marks ,result)
student = {
"john" : 65,
            "mary" : 82,
            "ali" : 55,
            "siam" : 90,
        }
print_results(student)
