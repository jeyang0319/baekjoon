# 15654

import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
stack = []
def bt():
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(0, n):
        if lst[i] not in stack:
            stack.append(lst[i])
            bt()
            stack.pop()

bt()