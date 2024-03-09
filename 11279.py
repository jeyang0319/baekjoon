# 11279

import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    num = (int(sys.stdin.readline().rstrip()) * -1)
    if num == 0:
        if len(lst) == 0:
            print(0)
        else:
            a = heapq.heappop(lst)
            print(-a)
    else:
        heapq.heappush(lst, num)