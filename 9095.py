# 9095
import sys

t = int(sys.stdin.readline())

lst = [1, 2, 4]

for i in range(4, 11):
    lst.append(sum(lst[-3:]))

for _ in range(t):
    n = int(sys.stdin.readline())
    print(lst[n-1])