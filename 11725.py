# 11725

import sys
from collections import deque

n = int(sys.stdin.readline())
network = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    network[u].append(v)
    network[v].append(u)

def dfs():
    d = deque()
    d.append(1)
    while d:
        s = d.popleft()
        visited[s] = True
        for i in network[s]:
            if not visited[i]:
                ans[i] = s
                d.append(i)

dfs()
print(*ans[2:], sep="\n")