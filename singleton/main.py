from random import randint


class SingletonMeta(type):

    _instances = []

    def __call__(cls, *args, **kwargs):

        while len(cls._instances) < 10:
            instance = super().__call__(*args, **kwargs)
            cls._instances.append(instance)
        return cls

    @classmethod
    def get_all_instances(cls):
        return cls._instances


class Singleton(metaclass=SingletonMeta):

    @classmethod
    def get_instances(cls):
        return cls.get_all_instances()

    @classmethod
    def get_random_instance(cls):
        cls.__call__()
        i = randint(0, 9)
        return cls.get_all_instances()[i]

    @classmethod
    def get_instances_number(cls):
        return len(cls.get_all_instances())

    def some_business_logic(self):
        print('Some business logic')


if __name__ == "__main__":
    # Client's code:

    s1 = Singleton()
    s2 = Singleton()
    assert s1 == s2
    print(f'Instance s1 is the same as s2: {s1 == s2}')
    # Instance s1 is the same as s2: True

    print('')

    print('All Singleton\'s objects:')
    print(Singleton.get_instances())
    # [<__main__.Singleton object at 0x7f348c07f7d0>, <__main__.Singleton object at 0x7f348c07f890>, ... ]

    print('')

    print(f'Singleton\'s objects number: {Singleton.get_instances_number()}')
    # Singleton's objects number: 10

    print('')

    instance = Singleton.get_random_instance()
    print(f'Singleton\'s random instance: {instance}')
    # Singleton's random instance: <__main__.Singleton object at 0x7fb237f049d0>

    print('')

    instance.some_business_logic()
    # Some business logic
