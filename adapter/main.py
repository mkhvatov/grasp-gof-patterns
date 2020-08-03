from abc import ABC, abstractmethod


class Taschenrechner:
    """class "Calculator" with german interface"""

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def falten(self) -> int:
        return self.a + self.b

    def multiplizieren(self) -> int:
        return self.a * self.b


class BaseCalculator(ABC):
    """Calculator interface"""

    @abstractmethod
    def __init__(self, a: int, b: int):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def multiply(self):
        pass


class Calculator(BaseCalculator):
    """Adapter for Taschenrechner ("Calculator" with german interface)"""

    def __init__(self, a: int, b: int):
        super().__init__(a, b)
        self.external = Taschenrechner(a, b)

    def add(self):
        return self.external.falten()

    def multiply(self):
        return self.external.multiplizieren()


if __name__ == "__main__":
    # Client's code:

    calculator = Calculator(4, 5)
    sum = calculator.add()
    print(sum)  # 9

    multiplication = calculator.multiply()
    print(multiplication)  # 20
