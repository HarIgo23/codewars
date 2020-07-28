from itertools import cycle
# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.alphabet = list(alphabet)
        self.key = [alphabet.index(i) for i in key]

    def encode(self, text):
        return self.code(text)

    def decode(self, text):
        return self.code(text, -1)

    def code(self, text: str, sign: int = 1) -> str:
        """correct sign -1 or 1"""
        return "".join([self.alphabet[(self.alphabet.index(text[i]) + sign * self.key[i % len(self.key)]) % len(self.alphabet)]
                        if text[i] in self.alphabet else text[i] for i in range(len(text))])




abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode('codewars'), 'rovwsoiv')
print(c.decode('rovwsoiv'), 'codewars')

print(c.encode('waffles'), 'laxxhsj')
print(c.decode('laxxhsj'), 'waffles')

print(c.encode('CODEWARS'), 'CODEWARS')
print(c.decode('CODEWARS'), 'CODEWARS')

# best solution
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')

    def cipher(self, mode, t):
        return ''.join(self.alphabet[(self.alphabet.index(m) + mode * self.alphabet.index(k)) % len(self.alphabet)]
                       if m in self.alphabet else m for m, k in zip(t.decode('utf-8'), cycle(self.key))).encode('utf-8')

    def encode(self, t): return self.cipher(1, t)

    def decode(self, t): return self.cipher(-1, t)

