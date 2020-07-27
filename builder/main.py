from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def reset(self, type: str):
        pass

    @abstractmethod
    def add_cheese(self, weight: int):
        pass

    @abstractmethod
    def add_bacon(self, weight: int):
        pass

    @abstractmethod
    def add_pineapples(self, weight: int):
        pass

    @abstractmethod
    def add_mushrooms(self, weight: int):
        pass

    @abstractmethod
    def add_seafood(self, weight: int):
        pass

    @abstractmethod
    def get_result(self):
        pass


class Pizza:
    type: str = None

    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        _name = self.type.replace('_', ' ')
        return f'Pizza \"{_name.upper()}\"'


class PizzaBuilder(Builder):

    _result: Pizza = None

    def reset(self, type: str):
        self._result = Pizza(type)

    def add_cheese(self, weight: int):
        self._result.cheese = weight

    def add_bacon(self, weight: int):
        self._result.bacon = weight

    def add_pineapples(self, weight: int):
        self._result.pineapples = weight

    def add_mushrooms(self, weight: int):
        self._result.mushrooms = weight

    def add_seafood(self, weight: int):
        self._result.seafood = weight

    def get_result(self) -> Pizza:
        return self._result


class Director:

    _builder: Builder = None

    def __init__(self, builder: Builder):
        self._builder = builder

    def make(self, type: str):
        self._builder.reset(type)

        if type == 'bacon_with_mushrooms':
            self._builder.add_cheese(100)
            self._builder.add_bacon(50)
            self._builder.add_mushrooms(20)

        if type == 'seafood_with_pineapples':
            self._builder.add_cheese(100)
            self._builder.add_seafood(70)
            self._builder.add_pineapples(30)

        if type == 'pineapples':
            self._builder.add_cheese(100)
            self._builder.add_pineapples(80)

        return self._builder.get_result()


if __name__ == '__main__':
    # Client's code:

    builder = PizzaBuilder()
    director = Director(builder)

    # cooking pizza 'bacon_with_mushrooms'
    pizza_1 = director.make('bacon_with_mushrooms')
    print(pizza_1, f'properties: {pizza_1.__dict__}')
    # Pizza "BACON WITH MUSHROOMS" properties: {'type': 'bacon_with_mushrooms', 'cheese': 100, 'bacon': 50, 'mushrooms': 20}

    # cooking pizza 'seafood_with_pineapples'
    pizza_2 = director.make('seafood_with_pineapples')
    print(pizza_2, f'properties: {pizza_2.__dict__}')
    # Pizza "SEAFOOD WITH PINEAPPLES" properties: {'type': 'seafood_with_pineapples', 'cheese': 100, 'seafood': 70, 'pineapples': 30}

    # cooking pizza 'pineapples'
    pizza_3 = director.make('pineapples')
    print(pizza_3, f'properties: {pizza_3.__dict__}')
    # Pizza "PINEAPPLES" properties: {'type': 'pineapples', 'cheese': 100, 'pineapples': 80}
