from abc import ABC, abstractmethod
from typing import List
from enum import Enum


class State(Enum):
    DISABLED = 0
    ACTIVE = 1


class Mediator(ABC):

    _services: List["BaseService"]

    def __init__(self):
        self._services = list()

    @abstractmethod
    def add_service(self, service: "BaseService"):
        pass

    @abstractmethod
    def _change_service_state(self, service: "BaseService"):
        pass

    @abstractmethod
    def inform(self, service: "BaseService"):
        pass


class BaseService(ABC):

    state: State
    _mediator: Mediator

    def __init__(self, mediator: Mediator):
        self.state = State.DISABLED
        self._mediator = mediator
        self._mediator.add_service(self)

    def __repr__(self):
        return f'Calling {self.__class__.__name__}'

    def _inform(self):
        self._mediator.inform(self)

    def call(self):
        self.state = State.ACTIVE
        self._inform()
        print(self.__repr__())


class ConcreteMediator(Mediator):

    def add_service(self, service: BaseService):
        self._services.append(service)

    def _change_service_state(self, service: BaseService):
        for _service in self._services:
            if _service != service:
                _service.state = State.DISABLED

    def inform(self, service: BaseService):
        self._change_service_state(service)


class Taxi(BaseService):
    pass


class Repairer(BaseService):
    pass


class FlowerDelivery(BaseService):
    pass


if __name__ == '__main__':
    # Client's code:

    mediator = ConcreteMediator()

    taxi = Taxi(mediator)
    repairer = Repairer(mediator)
    flowers = FlowerDelivery(mediator)

    taxi.call()  # Calling Taxi
    print('Taxi: ', taxi.state)  # Taxi:  State.ACTIVE
    print('Repairer: ', repairer.state)  # Repairer:  State.DISABLED
    print('FlowerDelivery: ', flowers.state)  # FlowerDelivery:  State.DISABLED

    print('*'*40)

    repairer.call()  # Calling Repairer
    print('Taxi: ', taxi.state)  # Taxi:  State.DISABLED
    print('Repairer: ', repairer.state)  # Repairer:  State.ACTIVE
    print('FlowerDelivery: ', flowers.state)  # FlowerDelivery:  State.DISABLED
