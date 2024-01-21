# 1269

import sys

n, m = map(int, input().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

ans = list(set(A) ^ set(B))
print(len(ans))