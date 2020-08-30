from abc import abstractmethod, ABC


class BaseOven(ABC):

    state: "State"

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def chill(self):
        pass

    @abstractmethod
    def prepare_for_work(self):
        pass

    @abstractmethod
    def overheat(self):
        pass


class BaseState(ABC):

    @abstractmethod
    def chill(self, oven: BaseOven):
        pass

    @abstractmethod
    def prepare_for_work(self, oven: BaseOven):
        pass

    @abstractmethod
    def overheat(self, oven: BaseOven):
        pass


class State(BaseState):

    def chill(self, oven: BaseOven):
        oven.state = Cold()

    def prepare_for_work(self, oven: BaseOven):
        oven.state = ReadyForWork()

    def overheat(self, oven: BaseOven):
        oven.state = Overheated()


class OvenException(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message


class Cold(State):

    def chill(self, oven: BaseOven):
        raise OvenException(message='The oven is already cold')


class ReadyForWork(State):

    def prepare_for_work(self, oven: BaseOven):
        raise OvenException(message='The oven is already ready for work')


class Overheated(State):

    def overheat(self, oven: BaseOven):
        raise OvenException(message='The oven is already overheated')


class Oven(BaseOven):

    state: State

    def __init__(self):
        self.state = Cold()

    def bake(self):
        if isinstance(self.state, ReadyForWork):
            print('Ready for work. Start baking pizza...')
        else:
            raise OvenException('Oven is not ready for work')

    def chill(self):
        self.state.chill(self)

    def prepare_for_work(self):
        self.state.prepare_for_work(self)

    def overheat(self):
        self.state.overheat(self)


def bake_pizza(oven: Oven):
    try:
        oven.bake()
    except OvenException as error:
        print(error.message)


if __name__ == '__main__':
    # Client's code:

    oven = Oven()
    bake_pizza(oven)
    # Oven is not ready for work

    print('*'*50)

    oven.prepare_for_work()
    bake_pizza(oven)
    # Ready for work. Start baking pizza...

    print('*'*50)

    oven.overheat()
    bake_pizza(oven)
    # Oven is not ready for work

    print('*'*50)
