import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from abc import ABC, abstractmethod

from facade.main import Calculator


class BaseCalculator(ABC):

    @abstractmethod
    def add(self, a: int, b: int) -> int:
        """Adds two numbers"""
        pass

    @abstractmethod
    def divide(self, a: int, b: int) -> int:
        """Divides number a by number b"""
        pass

    @abstractmethod
    def multiply(self, a: int, b: int) -> int:
        """Multiplies two numbers"""
        pass

    @abstractmethod
    def subtract(self, a: int, b: int) -> int:
        """Subtracts b from a"""
        pass


class CalculatorCache(BaseCalculator):
    """Cache proxy for Calculator class"""

    calculator: Calculator
    cache: dict

    def __init__(self):
        self.calculator = Calculator()
        self.cache = dict()

    def _set_value(self, key: str, value: int):
        self.cache[key] = value

    def get_value(self, key: str, a: int, b: int, command) -> int:
        """Gets value from cache or calculate it remote.
        command: method from Calculator class, for example: self.calculator.add"""

        value = self.cache.get(key)
        if not value:
            print('Calculate value remote...')
            value = command(a, b)
            print('Save value to local cache...')
            self._set_value(key, value)
        return value

    def add(self, a: int, b: int) -> int:
        key = f'{a}+{b}'
        value = self.get_value(key, a, b, command=self.calculator.add)
        return value

    def divide(self, a: int, b: int) -> int:
        key = f'{a}/{b}'
        value = self.get_value(key, a, b, command=self.calculator.divide)
        return value

    def multiply(self, a: int, b: int) -> int:
        key = f'{a}*{b}'
        value = self.get_value(key, a, b, command=self.calculator.multiply)
        return value

    def subtract(self, a: int, b: int) -> int:
        key = f'{a}-{b}'
        value = self.get_value(key, a, b, command=self.calculator.subtract)
        return value


if __name__ == "__main__":
    # Client's code:

    calculator = CalculatorCache()

    print(calculator.add(4, 5))
    # Calculate value remote...
    # Save value to local cache...
    # 9
    print(calculator.add(4, 5))
    # 9

    print(calculator.divide(10, 2))
    # Calculate value remote...
    # Save value to local cache...
    # 5
    print(calculator.divide(10, 2))
    # 5
