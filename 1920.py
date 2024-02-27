# 1920

import sys

n = int(sys.stdin.readline().rstrip())
lst = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())
find = map(int, sys.stdin.readline().split())

def binary_search(target):
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start + end) // 2
        if target == lst[mid]:
            return 1
        if target > lst[mid]:
            start = mid + 1
        else:
            end = mid-1
    return 0

for i in find:
    print(binary_search(i))