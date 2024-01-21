# 28278
import sys

n = int(input())

stack = []

def use_stack(num):
    if num[0] == '1':
        stack.append(num[1])
    elif num[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            ans = stack.pop()
            print(ans)
    elif num[0] == '3':
        print(len(stack))
    elif num[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == '5':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)
        
        
for i in range(n):
    q = sys.stdin.readline().split()
    use_stack(q)
    
