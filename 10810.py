# 10810

import sys

n, m = map(int, sys.stdin.readline().split())

lst = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i-1, j):
        lst[x] = k

for i in lst:
    print(i, end=" ")