from functools import wraps
from typing import Dict, Type

instances: Dict[Type, object] = {}


def singleton(class_):
    @wraps(class_)
    def decorator(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return decorator


class Singleton(type):

    def __new__(mcs, *args, **kwargs):
        if mcs not in instances:
            instances[mcs] = super().__new__(mcs, *args, **kwargs)
        return instances[mcs]
