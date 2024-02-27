# 10828

import sys

n = int(sys.stdin.readline().rstrip())

s = []
for _ in range(n):
    q = sys.stdin.readline().split()
    if q[0] == 'push':
        s.append(q[1])
    elif q[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif q[0] == 'size':
        print(len(s))
    elif q[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[len(s)-1])