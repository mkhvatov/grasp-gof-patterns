from abc import ABC, abstractmethod

from zeep import (
    Client,
    exceptions,
)


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


class Calculator(BaseCalculator):
    """Facade class for calculator web service (http://www.dneonline.com/calculator.asmx)"""

    WSDL = 'http://www.dneonline.com/calculator.asmx?WSDL'
    client = Client(wsdl=WSDL).service

    @staticmethod
    def _calculate(a: int, b: int, command):
        """command: client with operation name from wsdl file;
        for example: self.client.Add"""

        request_params = {
            'intA': a,
            'intB': b,
        }

        try:
            return command(**request_params)
        except exceptions.Fault as error:
            print(error.message)

    def add(self, a: int, b: int) -> int:
        """Adds two numbers"""
        return self._calculate(a, b, command=self.client.Add)

    def divide(self, a: int, b: int) -> int:
        """Divides number a by number b"""
        return self._calculate(a, b, command=self.client.Divide)

    def multiply(self, a: int, b: int) -> int:
        """Multiplies two numbers"""
        return self._calculate(a, b, command=self.client.Multiply)

    def subtract(self, a: int, b: int) -> int:
        """Subtracts b from a"""
        return self._calculate(a, b, command=self.client.Subtract)


if __name__ == "__main__":
    # Client's code:

    calculator = Calculator()

    print(calculator.add(4, 5))  # 9
    print(calculator.divide(10, 2))  # 5
    print(calculator.multiply(5, 2))  # 10
    print(calculator.subtract(7, 3))  # 4
