# 11047

import sys

n, k = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)
    
lst.sort(reverse=True)

cnt = 0
for i in lst:
    if i <= k:
        cnt += k // i
        k %= i

print(cnt)