# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

# def hamming(n):
#     res, prev, nums = [1], [1, 1, 1], [2, 3, 5]
#     for _ in range(n):
#         cur = [i * j for i, j in zip(prev, nums)]
#         res_item = min(cur)
#         res.append(res_item)
#         prev = [res[res.index(prev[i]) + 1] if cur[i] == res_item else prev[i] for i in range(3)]
#     return res[n-1]


# algo with cache
cache = {'res': [1], 'prev': [1, 1, 1]}


def hamming(n):
    res, prev, nums = cache['res'], cache['prev'], [2, 3, 5]
    if len(res) < n:
        for _ in range(len(res) - 1, n):
            cur = [i * j for i, j in zip(prev, nums)]
            res_item = min(cur)
            res.append(res_item)
            prev = [res[res.index(prev[i]) + 1] if cur[i] == res_item else prev[i] for i in range(3)]
        cache['res'], cache['prev'] = res, prev
    return res[n-1]
# it[it.index(num) + 1]


print(hamming(1) == 1, "hamming(1) should be 1")
print(hamming(2) == 2, "hamming(2) should be 2") 
print(hamming(3) == 3, "hamming(3) should be 3") 
print(hamming(4) == 4, "hamming(4) should be 4") 
print(hamming(5) == 5, "hamming(5) should be 5") 
print(hamming(6) == 6, "hamming(6) should be 6") 
print(hamming(7) == 8, "hamming(7) should be 8") 
print(hamming(8) == 9, "hamming(8) should be 9") 
print(hamming(9) == 10, "hamming(9) should be 10") 
print(hamming(10) == 12, "hamming(10) should be 12") 
print(hamming(11) == 15, "hamming(11) should be 15") 
print(hamming(12) == 16, "hamming(12) should be 16") 
print(hamming(13) == 18, "hamming(13) should be 18") 
print(hamming(14) == 20, "hamming(14) should be 20") 
print(hamming(15) == 24, "hamming(15) should be 24") 
print(hamming(16) == 25, "hamming(16) should be 25") 
print(hamming(17) == 27, "hamming(17) should be 27") 
print(hamming(18) == 30, "hamming(18) should be 30") 
print(hamming(19) == 32, "hamming(19) should be 32")
print(hamming(5000))

# best solution
def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

