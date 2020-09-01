from abc import abstractmethod, ABC
from typing import Dict, Any


class Strategy(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass


class SortStrategy(Strategy):

    def execute(self, array: list) -> list:
        return self._sort(array)

    @abstractmethod
    def _sort(self, array: list) -> list:
        pass


class QuickSortStrategy(SortStrategy):

    def _sort(self, array: list) -> list:
        n = len(array)
        self._quick_sort(array, 0, n - 1)
        return array

    def _quick_sort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pi = self._partition(array, low, high)

            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)

    def _partition(self, array: list, low: int, high: int) -> int:
        i = (low - 1)
        pivot = array[high]

        for j in range(low, high):

            if array[j] < pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1


class BubbleSortStrategy(SortStrategy):

    def _sort(self, array: list) -> list:
        self._bubble_sort(array)
        return array

    @staticmethod
    def _bubble_sort(array: list) -> None:
        n = len(array)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


class Context:

    strategies: Dict[str, SortStrategy]

    def __init__(self):
        self.strategies = {
            'quick_sort': QuickSortStrategy(),
            'bubble_sort': BubbleSortStrategy(),
        }

    def sort_array(self, array: list, strategy: str) -> list:
        strategy = self.strategies[strategy]
        return strategy.execute(array)


if __name__ == '__main__':
    # Client's code:

    array = [64, 34, 25, 12, 22, 11, 90]

    context = Context()

    sorted_array = context.sort_array(array, 'quick_sort')
    print(sorted_array)  # [11, 12, 22, 25, 34, 64, 90]

    sorted_array = context.sort_array(array, 'bubble_sort')
    print(sorted_array)  # [11, 12, 22, 25, 34, 64, 90]
