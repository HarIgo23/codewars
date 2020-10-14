# https://www.codewars.com/kata/53efc28911c36ff01e00012c/train/python
import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    tracer = Tracer(func)
    sys.settrace(tracer.my_tracer)
    rv = func(*args, **kwargs)
    return tracer.count, rv


class Tracer:
    count: int = 0
    func_name: str
    recursive: bool = False

    def __init__(self, func: callable):
        self.func_name = func.__name__

    def my_tracer(self, frame, event, arg=None):
        func_name = frame.f_code.co_name
        if event == 'call' and (self.recursive or func_name != self.func_name):
            self.count += 1
        elif func_name == self.func_name and not self.recursive:
            self.recursive = True
        return self.my_tracer


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


def rec(i):
    if i == 0:
        return 1
    return rec(i-1) + 1


print(count_calls(add, 8, 12))
print(count_calls(add_ten, 5))
print(count_calls(misc_fun))
print(count_calls(rec, 10))


# best solution
def count_calls(func, *args, **kwargs):
    """Count calls in function func"""

    calls = [-1]

    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer

    sys.settrace(tracer)

    rv = func(*args, **kwargs)

    return calls[0], rv
