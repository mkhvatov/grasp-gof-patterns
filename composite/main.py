from abc import ABC, abstractmethod
from typing import List


class Element(ABC):

    i: int = 0

    @abstractmethod
    def increment(self):
        pass

    @abstractmethod
    def decrement(self):
        pass


class Leaf(Element):

    def increment(self):
        self.i += 1

    def decrement(self):
        self.i -= 1


class Node(Element):

    def __init__(self):
        self._children: List[Element] = []

    def add_child(self, child: Element):
        self._children.append(child)

    def remove_child(self, child: Element):
        try:
            self._children.remove(child)
        except ValueError:
            print(f'Element {child} is not child of {self}')

    def increment(self):
        self.i += 1
        for child in self._children:
            child.increment()

    def decrement(self):
        self.i -= 1
        for child in self._children:
            child.decrement()


if __name__ == "__main__":
    # Client's code:

    main_element = Node()

    leaf_1 = Leaf()
    node_1 = Node()
    main_element.add_child(leaf_1)
    main_element.add_child(node_1)

    leaf_2 = Leaf()
    node_2 = Node()
    node_1.add_child(leaf_2)
    node_1.add_child(node_2)

    leaf_3 = Leaf()
    node_3 = Node()
    node_2.add_child(leaf_3)
    node_2.add_child(node_3)

    main_element.increment()

    print(main_element.i)  # 1
    print(leaf_1.i)  # 1
    print(node_1.i)  # 1
    print(leaf_2.i)  # 1
    print(node_2.i)  # 1
    print(leaf_3.i)  # 1
    print(node_3.i)  # 1

    main_element.decrement()

    print(main_element.i)  # 0
    print(leaf_1.i)  # 0
    print(node_1.i)  # 0
    print(leaf_2.i)  # 0
    print(node_2.i)  # 0
    print(leaf_3.i)  # 0
    print(node_3.i)  # 0
