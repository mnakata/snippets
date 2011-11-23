#!/usr/local/bin/python3.2 -t

import math
import random


N, M = 100, 10000
A, B = 0, 1000


def binrand():
    if random.random() < 0.5:
        return 0
    else:
        return 1

def rand(a, b):
    n = b - a + 1
    while 1:
        i, j = 1, 0
        while i < n:
            j += binrand() * i
            i <<= 1
        if j <= n:
            return j + a

if __name__ == '__main__':
    for i in range(N):
        while 1:
            a, b = random.randint(A, B), random.randint(A, B)
            if a < b:
                break

        rs = tuple(rand(a, b) for j in range(M))

        m = sum(rs) / M

        v = sum((r - m) ** 2 for r in rs) / M
        
        sd = math.sqrt(v)
        
        print('%d %d %.2f %.2f %.2f %.2f' % (a, b, m, v, sd, sd / (b - a + 1)))
