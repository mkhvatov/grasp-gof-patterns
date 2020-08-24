from abc import ABC, abstractmethod
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


class BaseExpression(ABC):
    invoker: Invoker
    commands: dict

    def __init__(self, invoker):
        self.invoker = invoker
        self.commands = dict()

    @abstractmethod
    def run(self, command: str) -> Pizza:
        pass

    @abstractmethod
    def _parse_command(self, command: str):
        pass

    @abstractmethod
    def _cook_pizza(self) -> Pizza:
        pass


class Expression(BaseExpression):

    def run(self, command: str) -> Pizza:  # command is string like 'Cheese 100, Mushrooms 30, Bacon 70'
        """command is string like 'Cheese 100, Mushrooms 30, Bacon 70' (part and weight of pizza)"""
        self._parse_command(command)
        return self._cook_pizza()

    def _parse_command(self, command: str):
        """Parse and save pizza's part and its weight to self.commands"""
        self.commands.clear()

        for item in command.split(', '):
            part, weight = item.split(" ")
            self.commands[part] = int(weight)

    def _cook_pizza(self) -> Pizza:
        """Create pizza and adds parts"""
        pizza = Pizza()
        for part, weight in self.commands.items():
            command = self._create_concrete_command_class(part)
            self.invoker.add_part(pizza, command, weight)
        return pizza

    @staticmethod
    def _create_concrete_command_class(part: str) -> type:
        return type(part, (Command,), dict())


if __name__ == '__main__':
    # Client's code:

    invoker = Invoker()
    expression = Expression(invoker)

    pizza_1 = expression.run('Cheese 100, Mushrooms 30, Bacon 70')
    print(pizza_1)
    # Pizza "CHEESE, MUSHROOMS, BACON" properties: {'cheese': 100, 'mushrooms': 30, 'bacon': 70}

    pizza_2 = expression.run('Cheese 100, Seafood 70, Pineapples 30')
    print(pizza_2)
    # Pizza "CHEESE, SEAFOOD, PINEAPPLES" properties: {'cheese': 100, 'seafood': 70, 'pineapples': 30}
