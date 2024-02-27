# 11399

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
result = 0
lst = []
for i in p:
    result += i
    lst.append(result)

print(sum(lst))