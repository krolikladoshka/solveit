import inspect
from collections import defaultdict
from functools import wraps
from types import FunctionType
from typing import Type


def method_calls_counter(cls: Type):
    def counter_decorator(func):
        @wraps(func)
        def counter(*args, **kwargs):
            cls.__calls_counter__[func.__name__] += 1

            return func(*args, **kwargs)

        counter.calls = 0

        return counter

    setattr(cls, '__calls_counter__', defaultdict(int))
    for name, attr in cls.__dict__.items():
        if isinstance(attr, FunctionType):
            setattr(cls, name, counter_decorator(attr))
            cls.__calls_counter__[name] = 0

    return cls


def bound_method_calls_counter(cls: Type):
    def counter_decorator(func):
        @wraps(func)
        def counter(*args, **kwargs):
            self, *rest = args
            self.__calls_counter__[func.__name__] += 1

            return func(self, *rest, **kwargs)

        counter.calls = 0

        return counter

    calls_counter = defaultdict(int)
    for name, attr in cls.__dict__.items():
        if isinstance(attr, FunctionType):
            setattr(cls, name, counter_decorator(attr))
            calls_counter[name] = 0

    @wraps(cls)
    def class_wrapper(*args, **kwargs):
        self = cls(*args, **kwargs)
        self.__calls_counter__ = calls_counter

        return self

    return class_wrapper


def test_method_calls_counter():
    @method_calls_counter
    class Test:
        def __init__(self):
            pass

        def method_a(self):
            print('a')

        def method_b(self):
            print('b')

        @staticmethod
        def test():
            print('static test')

        def __call__(self):
            print('__call__')

    test = Test()

    test.method_a()
    test.method_b()
    test.method_b()
    test()

    test2 = Test()
    test2.method_b()
    test2()
    test2()

    print(test.__calls_counter__)
    print(test2.__calls_counter__)



def test_bound_method_calls_counter():
    @bound_method_calls_counter
    class Test:
        def __init__(self):
            pass

        def method_a(self):
            print('a')

        def method_b(self):
            print('b')

        @staticmethod
        def test():
            print('static test')

        def __call__(self):
            print('__call__')

    test = Test()

    test.method_a()
    test.method_b()
    test.method_b()
    test()

    test2 = Test()
    test2.method_b()
    test2()
    test2()

    print(test.__calls_counter__)
    print(test2.__calls_counter__)

