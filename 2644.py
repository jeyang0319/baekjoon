# 2644

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
cnt = [0] * (n+1)

def dfs(x):
    visited[x] = True
    
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            cnt[i] = cnt[x] + 1
            dfs(i)

dfs(a)
if cnt[b] == 0:
    print(-1)
else:
    print(cnt[b])