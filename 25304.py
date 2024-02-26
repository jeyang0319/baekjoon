# 25304

import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x = x - (a*b)

if x == 0:
    print("Yes")
else:
    print("No")