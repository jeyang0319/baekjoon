# 5597

import sys

lst = [0] * 30

for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    lst[n-1] = 1

for i in range(len(lst)):
    if lst[i] == 0:
        print(i+1)