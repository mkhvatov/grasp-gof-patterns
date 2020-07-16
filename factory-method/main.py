from abc import ABC
from typing import Optional


class Dish(ABC):
    """Base class for specific dishes"""

    name = 'abstract dish'

    def __init__(self):
        print(self.__repr__())

    def __repr__(self):
        return f'Hi! I\'m {self.name} and I\'m ready!'


class FriedPotatoes(Dish):
    name = 'fried potatoes'


class Pie(Dish):
    name = 'pie'


class Jam(Dish):
    name = 'jam'


SETTINGS = {
    'potatoes': FriedPotatoes,
    'dough': Pie,
    'apples': Jam,
}


class Stove:
    """Stove cooks specific dishes depending on incoming parameters"""
    def __init__(self, settings: dict):
        self.SETTINGS = settings

    def cook(self, ingredient: str) -> Optional[Dish]:
        """Factory method. Returns class instance of specific dish.
        Returns None if ingredient is not in settings"""

        try:
            dish = self.SETTINGS[ingredient]
            return dish()
        except KeyError:
            print(f'Sorry, ingredient \'{ingredient}\' is missing in stove\'s settings')
            return None


if __name__ == '__main__':
    # Client's code:

    stove = Stove(SETTINGS)

    ingredients = ['potatoes', 'dough', 'apples', 'milk']

    for ingredient in ingredients:
        stove.cook(ingredient)
