from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def accept(self, visitor: "Visitor"):
        pass


class Pizza(Element):

    properties: dict

    def __init__(self):
        self.properties = dict()

    def __repr__(self):
        parts = ', '.join([key for key in self.properties.keys()]).upper()
        return f"Pizza \"{parts}\" properties: {self.properties}"

    def accept(self, visitor: "Visitor"):
        visitor.visit_pizza(self)


class Visitor(ABC):

    @abstractmethod
    def visit_pizza(self, element: Pizza):
        pass


class PizzaVisitor(Visitor):

    def __init__(self, weight: int):
        self.weight = weight

    def visit_pizza(self, element: Pizza):
        ingredient = self.__class__.__name__.lower()
        element.properties[ingredient] = self.weight


if __name__ == '__main__':
    # Client's code:

    pizza_1 = Pizza()
    ingredients_1 = {
        "Cheese": 100,
        "Bacon": 70,
        "Mushrooms": 30,
    }
    visitors_1 = [type(k, (PizzaVisitor,), dict())(v) for k, v in ingredients_1.items()]

    for visitor in visitors_1:
        pizza_1.accept(visitor)

    print(pizza_1)
    # Pizza "CHEESE, BACON, MUSHROOMS" properties: {'cheese': 100, 'bacon': 70, 'mushrooms': 30}

    print('*'*50)

    pizza_2 = Pizza()
    ingredients_2 = {
        "Cheese": 110,
        "Seafood": 80,
        "Pineapples": 40,
    }
    visitors_2 = [type(k, (PizzaVisitor,), dict())(v) for k, v in ingredients_2.items()]

    for visitor in visitors_2:
        pizza_2.accept(visitor)

    print(pizza_2)
    # Pizza "CHEESE, SEAFOOD, PINEAPPLES" properties: {'cheese': 110, 'seafood': 80, 'pineapples': 40}
