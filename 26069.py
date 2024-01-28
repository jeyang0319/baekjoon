# 26069
import sys

n = int(sys.stdin.readline().rstrip())
lst = set()
lst.add('ChongChong')
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if a in lst:
        lst.add(b)
    elif b in lst:
        lst.add(a)

print(len(lst))