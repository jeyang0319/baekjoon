# 11004
import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

print(lst[m-1])