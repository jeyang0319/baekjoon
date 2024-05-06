# 1766
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
lst = []
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(lst, (a, b))


print(heapq.heappop(lst))
print(heapq.heappop(lst))