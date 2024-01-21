# 11651

import sys

n = int(input())
li = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x, y])

li.sort(key = lambda x: (x[1], x[0]))
for i in li:
    print(i[0], i[1])