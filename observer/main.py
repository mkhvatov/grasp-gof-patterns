from abc import abstractmethod, ABC
from typing import List


class BaseObserver(ABC):

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass


class Subject(ABC):

    observers: List[BaseObserver]

    def __init__(self):
        self.observers = []

    @abstractmethod
    def add_observer(self, observer: BaseObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: BaseObserver):
        pass


class StormNotifier(Subject):

    hazard_level: int = 0

    def add_observer(self, observer: BaseObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: BaseObserver):
        self.observers.remove(observer)

    def change_hazard_level(self, level: int):
        self.hazard_level = level

        for observer in self.observers:
            observer.notify(level=self.hazard_level)


class Observer(BaseObserver):

    acceptable_level: int

    def notify(self, level: int):
        if level >= self.acceptable_level:
            self.react_to_hazard()

    def react_to_hazard(self):
        print(f'{self.__class__.__name__.upper()}: Danger! The storm begins!')


class School(Observer):
    acceptable_level: int = 4


class Airport(Observer):
    acceptable_level: int = 5


class RoadService(Observer):
    acceptable_level: int = 6


if __name__ == '__main__':
    # Client's code:

    storm_notifier = StormNotifier()

    school = School()
    storm_notifier.add_observer(school)

    airport = Airport()
    storm_notifier.add_observer(airport)

    road_service = RoadService()
    storm_notifier.add_observer(road_service)

    storm_notifier.change_hazard_level(3)
    print('*'*50)

    storm_notifier.change_hazard_level(4)
    # SCHOOL: Danger! The storm begins!
    print('*'*50)

    storm_notifier.change_hazard_level(5)
    # SCHOOL: Danger! The storm begins!
    # AIRPORT: Danger! The storm begins!
    print('*'*50)

    storm_notifier.change_hazard_level(6)
    # SCHOOL: Danger! The storm begins!
    # AIRPORT: Danger! The storm begins!
    # ROADSERVICE: Danger! The storm begins!
