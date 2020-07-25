from abc import ABC, abstractmethod
from typing import List


class TraditionalDish(ABC):
    """Base class for traditional dish"""
    name = "traditional dish"


class Lunch(ABC):
    """Base class for lunch"""
    name = "lunch"


class Cafe(ABC):
    """Abstract Factory. Base class for specific country food"""
    name = "cafe"
    traditional_dishes: List[TraditionalDish] = []

    @abstractmethod
    def cook_lunch(self) -> Lunch:
        pass


class JapanDish(TraditionalDish):
    name = "japan traditional dish"


class AmericanDish(TraditionalDish):
    name = "american traditional dish"


class UkrainianDish(TraditionalDish):
    name = "ukrainian traditional dish"


class JapanLunch(Lunch):
    name = "japan lunch"


class AmericanLunch(Lunch):
    name = "american lunch"


class UkrainianLunch(Lunch):
    name = "ukrainian lunch"


class JapanFood(Cafe):
    name = "cafe's japan food"
    traditional_dishes: List[JapanDish] = [JapanDish, ]

    def cook_lunch(self) -> JapanLunch:
        return JapanLunch()


class AmericanFood(Cafe):
    name = "cafe's american food"
    traditional_dishes: List[AmericanDish] = [AmericanDish, ]

    def cook_lunch(self) -> AmericanLunch:
        return AmericanLunch()


class UkrainianFood(Cafe):
    name = "cafe's ukrainian food"
    traditional_dishes: List[UkrainianDish] = [UkrainianDish, ]

    def cook_lunch(self) -> UkrainianLunch:
        return UkrainianLunch()


if __name__ == '__main__':
    # Client's code:

    SETTINGS = {
        'japan': JapanFood,
        'american': AmericanFood,
        'ukrainian': UkrainianFood,
    }

    for country_food in list(SETTINGS.values()):
        country_food = country_food()

        print('*' * 30)

        print([dish.name for dish in country_food.traditional_dishes])
        lunch = country_food.cook_lunch()
        print(lunch.name)
