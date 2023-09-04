class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def salary_raise(self):
        self.salary += 5000
