class Car:
    FUEL_TYPES = ['petrol', 'diesel', 'electric', 'hybrid']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = self.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS += 1
        self.numbers = Car.NUMBER_OF_CARS
        if color not in Car.COLORS:
            Car.COLORS.append(color)

    def __str__(self):
        return f'{self.numbers}: {self.model} - {self.year} - {self.fuel_type} - {self.color}'

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        if fuel_type in Car.FUEL_TYPES:
            return fuel_type
        else:
            return Car.FUEL_TYPES[0]

    def numbers(self):
        return f'{self.numbers} from {Car.NUMBER_OF_CARS}'

    @classmethod
    def get_used_colors(cls):
        return f'COLORS: {len(Car.COLORS)}'

    @classmethod
    def get_number_of_cars(cls):
        return F'NUMBER OF CARS: {Car.NUMBER_OF_CARS}'

a1 = Car('nissan', 2002, 'wight', 'q')
a2 = Car('bmw', 2010, 'red', 'diesel')
a3 = Car('lexus', 2024, 'wight', 'petrol')
a4 = Car('lexus', 2024, 'green', 'petrol')
print(a1.__dict__)
print(Car.NUMBER_OF_CARS)
print(Car.COLORS)
print(a1)
print(a2)

print(Car.numbers(a3))
print(Car.get_used_colors())
print(Car.get_number_of_cars())

for item in (a1, a2, a3, a4):
    print('item:', item)
    print('numbers:', item.numbers)


