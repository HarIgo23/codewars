# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python


def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    for el1, el2 in zip(sorted(array1, key=lambda el: abs(el)), sorted(array2)):
        if el1 * el1 != el2:
            return False
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2), True)
a1 = None
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = []
print(comp(a1, a2), False)
a1 = [121, 144, 19, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2), False)
a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2), True)


# best solution
def comp(a1, a2):
    return None not in (a1, a2) and [i * i for i in sorted(a1)] == sorted(a2)
