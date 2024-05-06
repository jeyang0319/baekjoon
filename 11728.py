# 11728

import sys

n, m = map(int, sys.stdin.readline().split())

lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(map(int, sys.stdin.readline().split()))
ans = []
a = b = 0
while (a < n) or (b < m):
    if a == n:
        ans.append(lst2[b])
        b += 1
        continue
    elif b == m:
        ans.append(lst1[a])
        a += 1
        continue
    elif lst1[a] < lst2[b]:
        ans.append(lst1[a])
        a += 1
        continue
    else:
        ans.append(lst2[b])
        b += 1
        continue

print(*ans)