# 1966

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    q = deque()
    idx = deque()
    a = list(map(int, sys.stdin.readline().split()))
    num = 0
    for i in a:
        q.append(i)
        idx.append(num)
        num += 1
    cnt = 0
    while True:
        if q[0] == max(q):
            q.popleft()
            ans = idx.popleft()
            cnt += 1
            if ans == m:
                print(cnt)
                break
        else:
            x = q.popleft()
            y = idx.popleft()
            q.append(x)
            idx.append(y)
    
    
    
    
    # for i in a:
    #     aa.append([i, num])
    #     q.append(num)
    #     num += 1
    #     idx.append(i)
    # bb = deque(sorted(aa, key = lambda x:(-x[0], x[1])))
    # print(bb)