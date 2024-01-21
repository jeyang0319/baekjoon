# 4949

import sys

while True:
    stack = []
    con = 1
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                con = 0
                break
            top = stack.pop()
            if top == '[':
                con = 0
                break
        elif i == ']':
            if len(stack) == 0:
                con = 0
                break
            top = stack.pop()
            if top == '(':
                con = 0
                break
    
    if len(stack) == 0 and con == 1:
        print("yes")
    else:
        print("no")
