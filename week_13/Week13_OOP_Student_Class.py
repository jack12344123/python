class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.course)
        print(self.marks)

    def check_pass(self):
        if self.marks >= 60:
            print("pass")
        else:
            print("fail")



student1 = Student('jack', 'Maths', 100)
student2 = Student('sam', 'sic', 70)
student3 = Student('zack', 'Maths', 80)


student1.display()
student1.check_pass()

student2.display()
student2.check_pass()

student3.display()
student3.check_pass()




