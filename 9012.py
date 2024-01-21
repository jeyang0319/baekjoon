# 9012

import sys

t = int(sys.stdin.readline())

for i in range(t):
    stack = []
    con = 1
    test = sys.stdin.readline().rstrip()
    for j in test:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                con = 0
                break
            else:
                stack.pop()
    
    if len(stack) == 0 and con == 1:
        print("YES")
    else:
        print("NO")