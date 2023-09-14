class Car:
    def __init__(self, brand, line, model, color):
        self.brand = brand
        self.line = line
        self.model = model
        self.color = color
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


my_car = Car("Audi", "A4", 2023, "Red")
my_car.turn_on()
my_car.turn_off()
