# https://www.codewars.com/kata/587a88a208236efe8500008b/train/python


def sequence_sum(b, e, s):
    if (s > 0 and b > e) or (s < 0 and b < e):
        return 0
    near = e - (e - b) % s
    n = (near - b) // s + 1
    return (b + near) * n // 2

# short version lambda
# sequence_sum = lambda b, e, s: 0 if (s > 0 and b > e) or (s < 0 and b < e) else (b + (e - (e - b) % s)) * (((e - (e - b) % s) - b) // s + 1) // 2


print(sequence_sum(2, 6, 2), 12, sequence_sum(2, 6, 2) == 12)
print(sequence_sum(1, 5, 1), 15, sequence_sum(1, 5, 1) == 15)
print(sequence_sum(1, 5, 3), 5, sequence_sum(1, 5, 3) == 5)
print(sequence_sum(-1, -5, -3), -5, sequence_sum(-1, -5, -3) == -5)
print(sequence_sum(16, 15, 3), 0, sequence_sum(16, 15, 3) == 0)
print(sequence_sum(-24, -2, 22), -26, sequence_sum(-24, -2, 22) == -26)
print(sequence_sum(-2, 4, 658), -2, sequence_sum(-2, 4, 658) == -2)
print(sequence_sum(780, 6851543, 5), 4694363402480, sequence_sum(780, 6851543, 5) == 4694363402480)
print(sequence_sum(9383, 71418, 2), 1253127200, sequence_sum(9383, 71418, 2) == 1253127200)
print(sequence_sum(20, 673388797, 5),  45345247259849570, sequence_sum(20, 673388797, 5) == 45345247259849570)


# best solution from codewars
def sequence_sum(a, b, step):
    n = (b-a)//step
    return 0 if n < 0 else (n+1)*(n*step+a+a)//2
