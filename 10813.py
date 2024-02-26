# 10813

import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(1,n+1):
    lst.append(i)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tmp = lst[a-1]
    lst[a-1] = lst[b-1]
    lst[b-1] = tmp
    
for j in lst:
    print(j, end = " ")