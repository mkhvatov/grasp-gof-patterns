from abc import abstractmethod, ABC
from datetime import datetime


class FileWriter(ABC):

    @staticmethod
    def _open_file():
        file = open("demo_file.txt", "a")
        return file

    @staticmethod
    def _close_file(file):
        file.close()

    @staticmethod
    def _write_to_file(file, info: str):
        file.write(info + '\n')

    @staticmethod
    @abstractmethod
    def _get_info(*args, **kwargs) -> str:
        pass

    def write(self, *args, **kwargs):
        file = self._open_file()
        info = self._get_info(*args, **kwargs)
        self._write_to_file(file, info)
        self._close_file(file)

    @staticmethod
    def print_file():
        file = open("demo_file.txt", "r")
        print(file.read())
        file.close()


class DateWriter(FileWriter):

    @staticmethod
    def _get_info(*args, **kwargs) -> str:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Current date: {current_date}"


class TimeWriter(FileWriter):

    @staticmethod
    def _get_info(*args, **kwargs) -> str:
        current_time = datetime.now().strftime("%H:%M")
        return f"Current time: {current_time}"


if __name__ == '__main__':
    # Client's code:

    date_writer = DateWriter()
    date_writer.write()
    date_writer.print_file()  # Current date: 02-09-2020

    time_writer = TimeWriter()
    time_writer.write()
    time_writer.print_file()
    # Current date: 02-09-2020
    # Current time: 00:18
