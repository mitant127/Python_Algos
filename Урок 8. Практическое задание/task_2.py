"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from heapq import heappush, heappop, heapify
from collections import defaultdict, Counter


def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    print(heap)
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


txt = "beep boop beer!"
symb2freq = Counter(txt)
huff = encode(symb2freq)
print(huff)
for i in txt:
    print(i)
    print(huff.index(), end=' ')

