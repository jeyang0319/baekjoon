# 11650

import sys

n = int(input())
li = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x, y])

li.sort()
for i in li:
    print(i[0], i[1])