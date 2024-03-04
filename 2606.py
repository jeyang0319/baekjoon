# 2606

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

network = {}
visitied = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u in network:
        network[u].append(v)
    else:
        network[u] = [v]
        
    if v in network:
        network[v].append(u)
    else:
        network[v] = [u]

def dfs(u):
    visitied[u] = True
    if u in network:
        for v in network[u]:
            if visitied[v] == False:
                dfs(v)

dfs(1)

print(visitied.count(True)-1)