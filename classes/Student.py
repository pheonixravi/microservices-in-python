class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

# Example usage:
student = Student("Scott", 15 , "10th")
student.display_info()