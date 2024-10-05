class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display_info(self):
        print(f"make:{self.make}")
        print(f"model:{self.model}")
class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self.num_doors=num_doors
    def additional_info(self):
        print(f"Num of Doors:{self.num_doors}")
class LuxuryCar(Car):
    def __init__(self,make,model,num_doors,features):
        super().__init__(make,model,num_doors)
        self.features=features
    def additional_info(self):
        super().additional_info()
        print(f"Features :{self.features}")
vechicle=Vehicle("Honda","Ek")
vechicle.display_info()

car=Car("Honda","Ek",4)
car.display_info()
car.additional_info()
  
Luxury_Car=LuxuryCar("Honda","EK",4,["Power","Speed","Anger Looks"])
Luxury_Car.display_info()
Luxury_Car.additional_info()
        
    
            