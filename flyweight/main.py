from abc import ABC, abstractmethod
from typing import Tuple, List


class SharedUnitInfo:

    def __init__(self, texture: str, sound: str):
        self._texture = texture
        self._sound = sound

    @property
    def texture(self):
        return self._texture

    @property
    def sound(self):
        return self._sound


class Unit(ABC):
    id: int
    coordinates: Tuple[int, int]
    shared_info: SharedUnitInfo

    def __init__(self, id: int, coordinates: Tuple[int, int], shared_info: SharedUnitInfo):
        self.id = id
        self.coordinates = coordinates
        self.shared_info = shared_info

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def shoot(self):
        pass


class Soldier(Unit):
    def move(self):
        """Concrete implementation for Soldier"""
        pass

    def shoot(self):
        """Concrete implementation for Soldier"""
        pass


class Tank(Unit):
    def move(self):
        """Concrete implementation for Tank"""
        pass

    def shoot(self):
        """Concrete implementation for Tank"""
        pass


class Army:
    name: str
    units: List[Unit]

    def __init__(self, name: str):
        self.name = name
        self.units = []

    def add_units(self, *args: Unit):
        for unit in args:
            self.units.append(unit)

    def set_coordinates(self, x: int, y: int):
        for unit in self.units:
            unit.coordinates = (x, y)


if __name__ == "__main__":
    # Client's code:

    soldier_info = SharedUnitInfo(texture='/textures/soldier.png', sound='/sound/soldier.mp3')
    tank_info = SharedUnitInfo(texture='/textures/tank.png', sound='/sound/tank.mp3')

    soldier_1 = Soldier(1, (1, 1), soldier_info)
    soldier_2 = Soldier(2, (2, 2), soldier_info)
    soldier_3 = Soldier(3, (3, 3), soldier_info)

    tank_1 = Tank(1, (1, 1), tank_info)
    tank_2 = Tank(2, (2, 2), tank_info)
    tank_3 = Tank(3, (3, 3), tank_info)

    army_1 = Army('First Army')
    army_2 = Army('Second Army')

    army_1.add_units(soldier_1, tank_1, tank_2)
    army_2.add_units(soldier_2, soldier_3, tank_3)

    army_1.set_coordinates(10, 10)
    army_2.set_coordinates(20, 20)

    for unit in army_1.units:
        assert unit.coordinates == (10, 10)
        print(unit.coordinates)  # (10, 10)

    for unit in army_2.units:
        assert unit.coordinates == (20, 20)
        print(unit.coordinates)  # (20, 20)
