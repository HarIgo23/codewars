# https://www.codewars.com/kata/53efc28911c36ff01e00012c/train/python
import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    tracer = Tracer()
    sys.settrace(tracer.my_tracer)
    rv = func(*args, **kwargs)
    return tracer.count, rv


class Tracer:
    count: int = -1

    def my_tracer(self, frame, event, arg=None):
        if event == 'call':
            self.count += 1
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
