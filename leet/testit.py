from copy import deepcopy
from importlib import import_module
from typing import List, Any


def call(module: str, solution_postfix: str, *args, **kwargs):
    module = import_module(f'leet.{module}')
    solution_class = getattr(module, 'Solution')
    function = [
        attr
        for attr in solution_class.__dict__.keys()
        if callable(getattr(solution_class, attr))
    ][0]

    return getattr(solution_class(), function)(*args, **kwargs)


def run(module: str, args_list: List[Any], output_formatter=print) -> object:
    for i, args in enumerate(args_list):
        args_copy = deepcopy(args)
        res = call(module, '', *args)
        print(f'Run {i + 1}, args {args_copy}:')
        output_formatter(res)


def print_matrix(res):
    for row in res:
        print(row)
