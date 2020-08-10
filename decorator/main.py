from abc import ABC


class AbstractPizza(ABC):

    def __init__(self):
        self.properties = dict()

    def __repr__(self):
        parts = ', '.join([key for key in self.properties.keys()]).upper()
        return f"Pizza \"{parts}\" properties: {self.properties}"


class Decorator(AbstractPizza):
    subject: AbstractPizza = None

    def __init__(self, subject: AbstractPizza, weight: int):
        super().__init__()
        self.subject = subject
        self.properties[self.part] = weight
        self.properties.update(self.subject.properties)

    @property
    def part(self):
        return self.__class__.__name__.lower()


class Pizza(AbstractPizza):
    pass


class Bacon(Decorator):
    pass


class Cheese(Decorator):
    pass


class Mushrooms(Decorator):
    pass


class Pineapples(Decorator):
    pass


class Seafood(Decorator):
    pass


if __name__ == '__main__':
    # Client's code:

    pizza_1 = Bacon(Mushrooms(Cheese(Pizza(), 200), 80), 90)
    print(pizza_1)
    # Pizza "BACON, MUSHROOMS, CHEESE" properties: {'bacon': 90, 'mushrooms': 80, 'cheese': 200}

    pizza_2 = Pineapples(Seafood(Cheese(Pizza(), 200), 90), 70)
    print(pizza_2)
    # Pizza "PINEAPPLES, SEAFOOD, CHEESE" properties: {'pineapples': 70, 'seafood': 90, 'cheese': 200}

    pizza_3 = Pineapples(Cheese(Pizza(), 200), 100)
    print(pizza_3)
    # Pizza "PINEAPPLES, CHEESE" properties: {'pineapples': 100, 'cheese': 200}
