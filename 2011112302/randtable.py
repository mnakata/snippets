#!/usr/local/bin/python3.2 -t

import itertools


N = 4


if __name__ == '__main__':
    for r in itertools.product((0, 1), repeat=N):
        for i in r:
            print(i, end=' ')
        print(sum(r))
