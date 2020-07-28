import re
# https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

# что-то придумать с дробными и отрицательными числами
# не работает нормально с отрицательными и дробными

'[\/\+\*\-\(\)]' # all operators
'\(.+\)' # expression in brackets
'\d+ [\/\*] \d+' # expression for mult and div
'\d+ [\+\-] \d+' # expression for mult and div


def div(operand_left, operand_right):
    return operand_left // operand_right


def mult(operand_left, operand_right):
    return operand_left * operand_right


def add(operand_left, operand_right):
    return operand_left + operand_right


def sub(operand_left, operand_right):
    return operand_left - operand_right


def search_in_brackets(s):
    left = re.search(r'\(', s).span()[0]
    right = left + 1
    flag = 1
    for i in range(right, len(s)+1):
        print(s[i: len(s)+1])
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
        oper = re.findall(r'[\/\+\*\-\(\)]', string)
        if len(re.findall(r'[\/\+\*\-]', string)) > len(re.findall(r'\d+', string)):
            return string
        if len(oper) < 1:
            return int(string)
        elif len(oper) == 1:
            nums = re.findall(r'\d+', string)
            return int(self.operations[oper[0]](int(nums[0]), int(nums[1])))
        while re.search(r'\(.+\)', string) is not None:
            rng = search_in_brackets(string)
            string = string[:rng[0]] + str(self.evaluate(string[rng[0]+1:rng[1]-1])) + string[rng[1]:]
        oper = re.findall(r'[\/\+\*\-\(\)]', string)
        if len(oper) < 1:
            return int(string)
        elif len(oper) == 1:
            nums = re.findall(r'\d+', string)
            return int(self.operations[oper[0]](int(nums[0]), int(nums[1])))
        while re.search(r'\d+ [\/\*] \d+', string) is not None:
            rng = re.search(r'\d+ [\/\*] \d+', string).span()
            string = string[:rng[0]] + str(self.evaluate(string[rng[0]:rng[1]])) + string[rng[1]:]
        if len(oper) < 1:
            return int(string)
        elif len(oper) == 1:
            nums = re.findall(r'\d+', string)
            return int(self.operations[oper[0]](int(nums[0]), int(nums[1])))
        while re.search(r'\d+ [\+\-] \d+', string) is not None:
            rng = re.search(r'\d+ [\+\-] \d+', string).span()
            string = string[:rng[0]] + str(self.evaluate(string[rng[0]:rng[1]])) + string[rng[1]:]
        return int(string)


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




