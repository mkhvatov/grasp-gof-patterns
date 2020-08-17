from typing import List
from abc import ABC


class CallHandler(ABC):
    next: List['CallHandler']
    _number: str = ''

    def __init__(self, *handlers: 'CallHandler'):
        self.next = [handler() for handler in handlers]

    def __call__(self, number: str):
        for handler in self.next:
            if handler._number == number:
                handler.process()
                break

    def process(self):
        print("Base call handler")


class AmbulanceHandler(CallHandler):
    _number = '03'

    def process(self):
        print("Call the ambulance")


class PoliceHandler(CallHandler):
    _number = '02'

    def process(self):
        print("Call the police")


class Firefighters(CallHandler):
    _number = '01'

    def process(self):
        print("Call the firefighters")


if __name__ == '__main__':
    # Client's code:

    call_handler = CallHandler(AmbulanceHandler, PoliceHandler, Firefighters)

    call_handler('03')  # Call the ambulance
    call_handler('01')  # Call the firefighters
    call_handler('02')  # Call the police
