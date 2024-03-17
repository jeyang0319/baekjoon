# 1753

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
r = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]
INF = sys.maxsize
distance = [INF] * (n+1)
distance[r] = 0

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((w, v))

q = []
heapq.heappush(q, (0, r))

while q:
    cost, node = heapq.heappop(q)
    
    if distance[node] < cost:
        continue
    
    for c, next_node in arr[node]:
        next_cost = cost + c
        if next_cost < distance[next_node]:
            distance[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))
            
for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)