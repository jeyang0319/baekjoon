# 1654

import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for _ in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

s, e = 1, max(lst)

while s <= e:
    mid = (s + e) // 2
    k = 0
    
    for i in lst:
        k += i // mid
    
    if k >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)

