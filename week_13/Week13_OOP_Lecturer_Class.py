# Create a class called Lecturer
class Lecturer:

    # Constructor method
    # This runs automatically when a new Lecturer object is created

    def __init__(self, Lecturer_name, Lecturer_age, department,course,years_experience):
        # Store the lecturer information inside the object

        self.Lecturer_name = Lecturer_name
        self.Lecturer_age = Lecturer_age
        self.department = department
        self.course = course
        self.years_experience = years_experience

    # Method to display lecturer information
    def printLecturer(self):
        print(self.Lecturer_name)
        print(self.Lecturer_age)
        print(self.department)
        print(self.course)
        print(self.years_experience)

    # Method to check if lecturer is experienced
    def check_experence(self):
        # Check years of experience
        if self.Lecturer_age >= 5:
            print("Experienced Lecturer")
        # Otherwise they are junior
        else:
            print("Junior Lecturer")


# Create a Lecturer object
Lecturer1 = Lecturer("jack88", 29, "maths", 5,20)
# Call the method to display lecturer information
Lecturer1.printLecturer()

# Call the method to check experience
Lecturer1.check_experence()







