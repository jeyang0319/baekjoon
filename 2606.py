# 2606

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

network = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    network[u].append(v)
    network[v].append(u)

def dfs(r):
    visited[r] = True
    for i in network[r]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)