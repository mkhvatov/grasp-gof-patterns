from abc import ABC
from typing import List


class Pizza:
    properties: dict

    def __init__(self):
        self.properties = dict()

    def __repr__(self):
        parts = ', '.join([key for key in self.properties.keys()]).upper()
        return f"Pizza \"{parts}\" properties: {self.properties}"


class Command(ABC):
    pizza: Pizza
    weight: int

    def __init__(self, pizza: Pizza, weight: int):
        self.pizza = pizza
        self.weight = weight

    @property
    def part(self) -> str:
        return self.__class__.__name__.lower()

    def execute(self):
        self.pizza.properties.setdefault(self.part, 0)
        self.pizza.properties[self.part] += self.weight

    def undo(self):
        if self.pizza.properties.get(self.part):
            diff = self.pizza.properties[self.part] - self.weight
            if diff <= 0:
                self.pizza.properties.pop(self.part)
            else:
                self.pizza.properties[self.part] = diff


class Invoker:
    list_undo: List[Command]
    list_redo: List[Command]

    def __init__(self):
        self.list_redo = list()
        self.list_undo = list()

    def add_part(self, pizza: Pizza, command: Command, weight: int):
        command = command(pizza, weight)
        command.execute()
        self.list_undo.append(command)

    def undo(self):
        if self.list_undo:
            command = self.list_undo[-1]
            command.undo()
            self.list_undo.remove(command)
            self.list_redo.append(command)

    def redo(self):
        if self.list_redo:
            command = self.list_redo[-1]
            command.execute()
            self.list_redo.remove(command)
            self.list_undo.append(command)


class Bacon(Command):
    pass


class Cheese(Command):
    pass


class Mushrooms(Command):
    pass


class Pineapples(Command):
    pass


class Seafood(Command):
    pass


if __name__ == '__main__':
    # Client's code:

    Invoker = Invoker()
    pizza_1 = Pizza()

    Invoker.add_part(pizza_1, Cheese, 100)
    Invoker.add_part(pizza_1, Bacon, 70)
    Invoker.add_part(pizza_1, Mushrooms, 30)
    print(pizza_1)
    # Pizza "CHEESE, BACON, MUSHROOMS" properties: {'cheese': 100, 'bacon': 70, 'mushrooms': 30}

    Invoker.undo()
    print(pizza_1)
    # Pizza "CHEESE, BACON" properties: {'cheese': 100, 'bacon': 70}

    Invoker.redo()
    print(pizza_1)
    # Pizza "CHEESE, BACON, MUSHROOMS" properties: {'cheese': 100, 'bacon': 70, 'mushrooms': 30}
