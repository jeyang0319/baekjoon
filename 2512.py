# 2512

import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())

s, e = 1, max(lst)

while s <= e:
    if sum(lst) <= m:
        e = max(lst)
        break
    mid = (s + e) // 2
    a = 0
    for i in lst:
        if i >= mid:
            a += mid
        else:
            a += i
            
    if a <= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)