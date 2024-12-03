import csv
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age )
        Employee.__init__(self,employee_id, position)
        self.department = department

    def display_info(self):

        Person.display_info(self)
        Employee.display_info(self)
        print(f"Department: {self.department}")

    def additional_info(self):
        return f"Department: {self.department}"

class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        try:
            with open(self.filename, mode='r', newline='') as file:
                pass
        except FileNotFoundError:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Age', 'Employee_ID', 'Position', 'Department'])
    
    def read_employees(self):
        employees = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                if row:
                    name, age, employee_id, position, department = row
                    employee = Staff(name, int(age), employee_id, position, department)
                    employees.append(employee)
        return employees

    def save_employees(self, employees):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Employee_ID', 'Position', 'Department'])
            for employee in employees:
                writer.writerow([employee.name, employee.age, employee.employee_id, employee.position, employee.department])

    def add_employee(self, name, age, employee_id, position, department):
        employees = self.read_employees() 
        new_employee = Staff(name, age, employee_id, position, department)
        employees.append(new_employee)
        self.save_employees(employees)  

manager = EmployeeManager()  

manager.add_employee('Ali', 22, '342', 'Developer', 'SEE')
manager.add_employee('Shuraim', 20, '908', 'Developer', 'Web designing')
manager.add_employee('Zabi',30,'576','Dveloper','Backend')

employees = manager.read_employees()
for employee in employees:
    employee.display_info()