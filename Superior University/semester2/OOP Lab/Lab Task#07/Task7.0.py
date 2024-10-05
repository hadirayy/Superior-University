class Employee:
    def __init__(self, name, position):
        self.name=name
        self.position=position
    def display_info(self):
        print(f"Name :{self.name}")
        print(f"Position:{self.position}")
class  Manager(Employee):
    def __init__(self,name,position,department):
        super().__init__(name,position)
        self.department=department
    def additional_info(self):
        print(f"Department:{self.department}")
class Worker(Employee):
    def __init__(self, name, position,hours_worked):
        super().__init__(name, position)
        self.hours_worked=hours_worked
    def additional_info(self):
        print(f"Hours Worked:{self.hours_worked}")
employee=Employee("Hadi","Manager")
employee.display_info()

manager=Manager("Hadi","Manager","Managment")
manager.display_info()
manager.additional_info()

worker= Worker("Hadi","Manager",10)
worker.display_info()
worker.additional_info()