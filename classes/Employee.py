class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def give_raise(self, amount):
        self.salary += amount

# Example usage:
employee = Employee("Vikas", 50000, "Software Engineer")
print("Initial salary:", employee.salary)
employee.give_raise(5000)
print("After raise:", employee.salary)
