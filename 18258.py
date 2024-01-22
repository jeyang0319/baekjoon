# 18258

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
lst = deque()

def use_queue(q):
    if q[0] == "push":
        lst.append(q[1])
    elif q[0] == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())
    elif q[0] == "size":
        print(len(lst))
    elif q[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif q[0] == "back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[len(lst) - 1])


for i in range(n):
    q = sys.stdin.readline().split()
    use_queue(q)