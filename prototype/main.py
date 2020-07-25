from typing import Optional
import copy


class Vehicle:
    color: str = 'white'
    number: str = 'v001'

    _prototypes_storage = {}

    def _clone(self, type: str, color: Optional[str], number: Optional[str]):
        """Make a shallow copy of entity. Use copy.deepcopy() if you need deep copy"""
        clon = copy.copy(self._prototypes_storage[type])
        if color:
            clon.color = color
        if number:
            clon.number = number
        return clon

    def add_type(self, type: str, entity):
        self._prototypes_storage[type] = entity()

    def get_car(self, color: Optional[str] = None, number: Optional[str] = None):
        return self._clone('car', color, number)

    def get_lorry(self, color: str = None, number: str = None):
        return self._clone('lorry', color, number)

    def get_minivan(self, color: str = None, number: str = None):
        return self._clone('minivan', color, number)


class Car(Vehicle):
    pass


class Lorry(Vehicle):
    pass


class Minivan(Vehicle):
    pass


if __name__ == '__main__':
    # Client's code:

    prototype = Vehicle()

    # add concrete car types to vehicle prototypes
    for type, entity in [('car', Car), ('lorry', Lorry), ('minivan', Minivan)]:
        prototype.add_type(type, entity)

    car = prototype.get_car()
    lorry = prototype.get_lorry(color='red', number='v123')
    minivan = prototype.get_minivan(number='v124')

    print(car, lorry, minivan)

    print('*' * 30)

    print('Car: ', car.color, car.number)
    print('Lorry: ', lorry.color, lorry.number)
    print('Minivan: ', minivan.color, minivan.number)
