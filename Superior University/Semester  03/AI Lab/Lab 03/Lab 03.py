class ModelAgent():
    def __init__(self):
        self.perivious_tem = None
        self.heater = "off"
    def update(self,current_temperature):
        if current_temperature < 20:
            if self.heater =="off":
                self.turn_heater_on()
        elif current_temperature > 22 :
            if self.heater == "on":
                self.turn_heater_off()
        self.perivious_tem = current_temperature
    def turn_heater_on(self):
        self.heater ="On"
        print("Heater is on")
    def turn_heater_off(self):
        self.heater = "Off"
        print("Heater is off")
Agent=ModelAgent()
Temperature=[20,34,21,45,19,99]
for temp in Temperature:
    print(f"Current temperature:{temp}C")
    Agent.update(temp)
    print(
        f"Current Heater:{Agent.heater}"
    )