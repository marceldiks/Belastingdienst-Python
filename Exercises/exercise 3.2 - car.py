class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def info(self):
        print( f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.' )

    def __str__(self):
        return f'{self._color} {self._make} {self._model} mileage: {self._mileage}km.'

    def __repr__(self):
        return f"Car('{self._make}', '{self._model}', '{self._color}', mileage={self._mileage})"

    def __int__(self):
        return self._mileage

    def drive(self, km):
        self._mileage += km
        print(f'Driving {km}km.')


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown')

    my_car.drive(200)
    my_car.drive(300)

    my_car.info()

    print(str(my_car))
    print(repr(my_car))
