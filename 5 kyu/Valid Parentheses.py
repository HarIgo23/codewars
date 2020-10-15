# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    counter = 0
    for el in string:
        if el == '(':
            counter += 1
        elif el == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


print(valid_parentheses("  ("), False)
print(valid_parentheses(")test"), False)
print(valid_parentheses(""), True)
print(valid_parentheses("hi())("), False)
print(valid_parentheses("hi(hi)()"), True)
