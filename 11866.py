# 11866

import sys

n, k = map(int, sys.stdin.readline().split())

lst = []
ans = []
for i in range(1, n + 1):
    lst.append(i)
    

idx = 0
while lst:
    idx += k - 1
    if idx >= len(lst):
        idx %= len(lst)
    ans.append(str(lst.pop(idx)))
    

print("<", ", ".join(ans), ">", sep="")