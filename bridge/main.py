from abc import ABC


class Meal(ABC):
    """Base class for specific kind of meal (1st, 2nd, etc)"""
    name = "base meal"

    def __init__(self, food: str):
        self._food = food

    def __repr__(self):
        return f"The {self.name} of {self._food}"


class FirstMeal(Meal):
    name = "first meal"


class SecondMeal(Meal):
    name = "second meal"


class ThirdMeal(Meal):
    name = "third meal"


class Dessert(Meal):
    name = "dessert"


class BaseFood(ABC):
    """Base class for specific country food"""
    name = "base food"

    _meal_kind = {
        'first': FirstMeal,
        'second': SecondMeal,
        'third': ThirdMeal,
        'dessert': Dessert,
    }

    def get_meal(self, kind: str):
        try:
            meal = self._meal_kind[kind]
            return meal(self.name)
        except KeyError:
            print(f'Sorry, \"{kind}\" is missing in meal\'s kinds')


class JapanFood(BaseFood):
    name = "japan food"


class AmericanFood(BaseFood):
    name = "american food"


class UkrainianFood(BaseFood):
    name = "ukrainian food"


if __name__ == "__main__":
    # Client's code:

    japan_first = JapanFood().get_meal('first')
    print(japan_first)
    # The first meal of japan food

    american_second = AmericanFood().get_meal('second')
    print(american_second)
    # The second meal of american food

    ukrainian_third = UkrainianFood().get_meal('third')
    print(ukrainian_third)
    # The third meal of ukrainian food

    japan_dessert = JapanFood().get_meal('dessert')
    print(japan_dessert)
    # The dessert of japan food
