# 1037
import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
print(lst[0] * lst[len(lst) - 1])