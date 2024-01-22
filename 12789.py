# 12789

import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

cnt = 1
stack = []

while lst:
    if lst[0] == cnt:
        lst.pop(0)
        cnt += 1
    else:
        stack.append(lst.pop(0))
    
    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break


if len(stack) == 0:
    print("Nice")
else:
    print("Sad")