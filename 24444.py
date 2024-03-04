# 24444

import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

network = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)
    
for i in range(n+1):
    network[i].sort()


def bfs(r):
    queue = deque()
    queue.append(r)
    global cnt
    while queue:
        q = queue.popleft()
        if not visited[q]:
            visited[q] = cnt
            cnt += 1
            for i in network[q]:
                if not visited[i]:
                    queue.append(i)

bfs(r)
print(*visited[1:], sep='\n')