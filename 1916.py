# 1916

import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n + 1)]
INF = sys.maxsize
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((w, v))

start, end = map(int, sys.stdin.readline().split())

q = []
heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)
    
    if node == end:
        print(cost)
        break
    
    if distance[node] < cost:
        continue
    
    for c, next_node in arr[node]:
        next_cost = cost + c
        if next_cost < distance[next_node]:
            distance[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))