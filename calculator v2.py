import re
# https://www.codewars.com/kata/5235c913397cbf2508000048/train/python


'[\/\+\*\-\(\)]' # all operators
'\(.+\)' # expression in brackets
'\d+ [\/\*] \d+' # expression for mult and div
'\d+ [\+\-] \d+' # expression for mult and div


def div(operand_left, operand_right):
    return operand_left / operand_right


def mult(operand_left, operand_right):
    return operand_left * operand_right


def add(operand_left, operand_right):
    return operand_left + operand_right


def sub(operand_left, operand_right):
    return operand_left - operand_right


def search_in_brackets(s):
    left = s.index('(')
    right = left + 1
    flag = 1
    for i in range(right, len(s)+1):
        if s[right] == ')':
            flag -= 1
        elif s[right] == '(':
            flag += 1
        right = i
        if flag == 0:
            return left, right


class Calculator(object):

    operations = {'*': mult, '/': div, '+': add, '-': sub}

    def evaluate(self, string):
        lfs = re.findall(r'\-*\d+\.\d+|\-*\d+|[\/\+\*\-\(\)]', string)
        oper = re.findall(r'[\/\+\*\-\(\)](?= )', string)
        if len(oper) < 1:
            return float(string)
        elif len(oper) == 1:
            return float(self.operations[lfs[1]](float(lfs[0]), float(lfs[2])))
        while '(' in lfs:
            rng = search_in_brackets(lfs)
            lfs = lfs[:rng[0]] + [str(self.evaluate(" ".join(lfs[rng[0]+1:rng[1]-1])))] + lfs[rng[1]:]
        while '*' in lfs or '/' in lfs:
            if len(lfs) == 3:
                return self.evaluate(' '.join(lfs))
            if '*' in lfs and '/' in lfs:
                ind = min(lfs.index('*'), lfs.index('/'))
            elif '*' in lfs:
                ind = lfs.index('*')
            else:
                ind = lfs.index('/')
            lfs = lfs[: ind-1] + [str(self.evaluate(" ".join(lfs[ind-1:ind+2])))] + lfs[ind+2:]
        while '+' in lfs or '-' in lfs:
            if len(lfs) == 3:
                return self.evaluate(' '.join(lfs))
            if '+' in lfs and '-' in lfs:
                ind = min(lfs.index('+'), lfs.index('-'))
            elif '+' in lfs:
                ind = lfs.index('+')
            else:
                ind = lfs.index('-')
            lfs = lfs[: ind - 1] + [str(self.evaluate(" ".join(lfs[ind - 1:ind + 2])))] + lfs[ind + 2:]
        return float(lfs[0])


calc = Calculator()

# simple test
print(calc.evaluate('2 + 2'))
print(calc.evaluate('9 / 3'))
print(calc.evaluate('7 * 3'))
print(calc.evaluate('8 - 2'))
# mul and division test
print(calc.evaluate('9 / 3 * 4'))
print(calc.evaluate('7 * 3 * 2 / 6'))
# brackets with mul and div
print(calc.evaluate('9 / (3 * 3)'))
print(calc.evaluate('54 / (3 * (10 / 5))'))
# add and sub
print(calc.evaluate('7 + 3 - 2 + 6'))
print(calc.evaluate('54 - (3 + (10 / 5))'))
print(calc.evaluate('2 / 2 + 3 * 4 - 6'))
print(calc.evaluate('-5.1 + 3 * -4'))

# best solution from codewars

from operator import add, sub, mul, truediv

FIRST = {'*' : mul, '/': truediv}
SECOND = {'+': add, '-': sub}

class Calculator(object):
    def evaluate(self, string):
        tokens = [float(t) if t.isdigit() or '.' in t else t for t in string.split()]
        while True:
            for (i, token) in enumerate(tokens):
                op = FIRST.get(token)
                if op:
                    tokens[i - 1 : i + 2] = [op(tokens[i - 1], tokens[i + 1])]
                    break
            else:
                ret = tokens[0]
                for i in range(1, len(tokens), 2):
                    ret = SECOND[tokens[i]](ret, tokens[i + 1])
                return ret


calc = Calculator()

# simple test
print(calc.evaluate('2 + 2'))
print(calc.evaluate('9 / 3'))
print(calc.evaluate('7 * 3'))
print(calc.evaluate('8 - 2'))
# mul and division test
print(calc.evaluate('9 / 3 * 4'))
print(calc.evaluate('7 * 3 * 2 / 6'))
# brackets with mul and div
print(calc.evaluate('9 / (3 * 3)'))
print(calc.evaluate('54 / (3 * (10 / 5))'))
# add and sub
print(calc.evaluate('7 + 3 - 2 + 6'))
print(calc.evaluate('54 - (3 + (10 / 5))'))
print(calc.evaluate('2 / 2 + 3 * 4 - 6'))
# print(calc.evaluate('-5.1 + 3 * -4')) # unsupport negative number for solution from codewars



