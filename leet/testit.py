import sys
import time
from copy import deepcopy
from importlib import import_module
from io import StringIO
from typing import List, Any


def solution_class_function_call(module: str, *args, **kwargs):
    module = import_module(module)
    solution_class = getattr(module, 'Solution')
    function = [
        attr
        for attr in solution_class.__dict__.keys()
        if callable(getattr(solution_class, attr))
    ][0]

    function = getattr(solution_class(), function)

    start = time.time()
    result = function(*args, **kwargs)
    end = time.time() - start

    return result, end


def stdin_stdout_execute_module(module: str, *args, mock_stdin: bool = True, **kwargs):
    args_count = len(args)
    args = '\n'.join(args)

    if 'many_cases' in kwargs:
        args = f'{args_count}\n{args}'

    old_stdin = sys.stdin
    old_stdout = sys.stdout

    if mock_stdin:
        sys.stdin = StringIO(args)
    sys.stdout = StringIO()

    start = time.time()
    import_module(module)
    end = time.time() - start

    del sys.modules[module]

    result = sys.stdout.getvalue()

    if mock_stdin:
        sys.stdin.close()
    sys.stdout.close()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    return result, end


runners = {
    'leet': solution_class_function_call,
    'codeforces': stdin_stdout_execute_module,
}


def call(module: str, *args, **kwargs):
    runner = module.split('.')[0]

    return runners[runner](module, *args, **kwargs)


def run(module: str, args_list: List[Any], output_formatter=print, **kwargs) -> object:
    for i, args in enumerate(args_list):
        args_copy = deepcopy(args)
        res, duration = call(module, *args, **kwargs)
        print(f'Run {i + 1}, args {args_copy}:')
        output_formatter(res)
        print(f'Execution time: {duration}')


def print_matrix(res):
    for row in res:
        print(row)
