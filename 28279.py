# 28279

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dec = deque()

def use_dec(q):
    if q[0] == '1':
        dec.appendleft(q[1])
    elif q[0] == '2':
        dec.append(q[1])
    elif q[0] == '3':
        if dec:
            print(dec.popleft())
        else:
            print(-1)
    elif q[0] == '4':
        if dec:
            print(dec.pop())
        else:
            print(-1)
    elif q[0] == '5':
        print(len(dec))
    elif q[0] == '6':
        if dec:
            print(0)
        else:
            print(1)
    elif q[0] == '7':
        if dec:
            print(dec[0])
        else:
            print(-1)
    elif q[0] == '8':
        if dec:
            print(dec[len(dec)-1])
        else:
            print(-1)



for _ in range(n):
    q = sys.stdin.readline().split()
    use_dec(q)