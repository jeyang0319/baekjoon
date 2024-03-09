# 1927

import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, num)
    