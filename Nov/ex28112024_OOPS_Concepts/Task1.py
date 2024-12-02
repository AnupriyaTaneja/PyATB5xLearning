# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
# Use PC - to set the value of the attributes
# create a Print student information method/function
# 3 students objects
# PyATB().print_student_infomation()

class PyATB:
    name = None
    job_role = None
    years_of_exp = None
    phone_num = None
    city = None

    def __init__(self, name, job_role, years_of_exp, phone_num, city):
        self.name = name
        self.job_role = job_role
        self.years_of_exp = years_of_exp
        self.phone_num = phone_num
        self.city = city


    def getName(self):
        return self.name

    def getJobRole(self):
        return self.job_role

    def getYearsOfExp(self):
        return self.years_of_exp

    def getPhoneNum(self):
        return self.phone_num

    def getCity(self):
        return self.city

    def print_student_info(self):
        print(self.name, self.job_role, self.years_of_exp, self.phone_num, self.city)


obj1 = PyATB("Anu", "TL", 10, 12345, "Delhi")
obj2 = PyATB("Priya", "TA", 7, 23456, "Kanpur")
obj3 = PyATB("Taneja", "TE", 2, 34567, "Hyderabad")

print("Student_Information1: ")
obj1.print_student_info()
print("********************")
print("Student_Information2: ")
obj2.print_student_info()
print("********************")
print("Student_Information3: ")
obj3.print_student_info()
print("********************")
