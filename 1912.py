# 1912
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    lst[i] = max(lst[i], lst[i-1] + lst[i])

print(max(lst))