# 1715

import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lst = []
answer = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    heapq.heappush(lst, num)
    
for _ in range(n-1):
    a = heapq.heappop(lst)
    answer.append(a)
    b = heapq.heappop(lst)
    answer.append(b)
    heapq.heappush(lst, a+b)

print(sum(answer))