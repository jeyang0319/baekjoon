# 24511

import sys
from collections import deque

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(input())
c = list(map(int, sys.stdin.readline().split()))

lst = deque()
for i in range(n):
    if a[i] == 0:
        lst.append(b[i])

for j in range(m):
    lst.appendleft(c[j])
    
for _ in range(m):
    print(lst.pop(), end=' ')