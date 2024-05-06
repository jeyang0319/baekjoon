#1182

import sys

n, s = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

stack = []
cnt = 0
def back(start):
    global cnt
    if (len(stack) > 0) and (sum(stack) == s):
        cnt += 1
    
    for i in range(start, n):
        stack.append(lst[i])
        back(i+1)
        stack.pop()

back(0)
print(cnt)