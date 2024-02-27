# 10845

import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()
for _ in range(n):
    q = sys.stdin.readline().split()
    if q[0] == 'push':
        d.append(q[1])
    elif q[0] == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif q[0] == 'size':
        print(len(d))
    elif q[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif q[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[len(d)-1])