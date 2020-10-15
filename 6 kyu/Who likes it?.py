# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python


def likes(names):
    if len(names) <= 1:
        return ("no one" if not names else names[0]) + " likes this"
    elif len(names) < 4:
        s = "{} and {}".format(*names) if len(names) == 2 else "{}, {} and {}".format(*names)
    else:
        s = f"{names[0]}, {names[1]} and {len(names)-2} others"
    return s + " like this"


print(likes([]), likes([]) == 'no one likes this')
print(likes(['Peter']), likes(['Peter']) == 'Peter likes this')
print(likes(['Jacob', 'Alex']), likes(['Jacob', 'Alex']) == 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']),
      likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this')

# best solution
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
