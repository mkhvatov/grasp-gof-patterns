from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Memento:

    _state: str

    def __init__(self, state):
        self._state = state

    @property
    def state(self) -> str:
        return self._state


class BaseOriginator(ABC):
    state: str

    @abstractmethod
    def create_memento(self) -> Memento:
        pass

    @abstractmethod
    def restore(self, memento: Memento):
        pass


class BaseCaretaker(ABC):

    _originator: BaseOriginator
    _archive: dict

    def __init__(self, originator: BaseOriginator):
        self._originator = originator
        self._archive = {}

    @abstractmethod
    def save_version(self):
        pass

    @abstractmethod
    def restore_version(self, version: str):
        pass


class Originator(BaseOriginator):

    def create_memento(self) -> Memento:
        return Memento(state=self.state)

    def restore(self, memento: Memento):
        self.state = memento.state


class Caretaker(BaseCaretaker):

    def save_version(self):
        memento = self._originator.create_memento()
        time = datetime.now().strftime("%d-%m-%Y_%H:%M")
        version = len(self._archive) + 1
        self._archive[f'{version}_{time}'] = memento

    def _get_version(self, version_name: str) -> Memento:
        return self._archive[version_name]

    def restore_version(self, version_name: str):
        version = self._get_version(version_name)
        self._originator.restore(version)

    @property
    def saved_versions(self) -> List[str]:
        return [key for key in self._archive.keys()]


if __name__ == '__main__':
    # Client's code:

    text_editor = Originator()
    caretaker = Caretaker(originator=text_editor)

    text_editor.state = 'Python is powerful... and fast;'
    caretaker.save_version()

    text_editor.state = 'Python is powerful... and fast;\n' \
                        'plays well with others;\nruns everywhere;'
    caretaker.save_version()

    text_editor.state = 'Python is powerful... and fast;\n' \
                        'plays well with others;\nruns everywhere;\n' \
                        'is friendly & easy to learn;\nis Open.'
    caretaker.save_version()

    saved_versions = caretaker.saved_versions
    print(saved_versions)  # ['1_29-08-2020_21:04', '2_29-08-2020_21:04', '3_29-08-2020_21:04']
    print('*' * 50)

    caretaker.restore_version(saved_versions[1])
    print(text_editor.state)
    # Python is powerful... and fast;
    # plays well with others;
    # runs everywhere;
    print('*'*50)

    caretaker.restore_version(saved_versions[0])
    print(text_editor.state)
    # Python is powerful... and fast;
    print('*'*50)

    caretaker.restore_version(saved_versions[2])
    print(text_editor.state)
    # Python is powerful... and fast;
    # plays well with others;
    # runs everywhere;
    # is friendly & easy to learn;
    # is Open.
