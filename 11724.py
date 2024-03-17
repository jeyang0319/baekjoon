# 11724

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)
    
cnt = 0

def dfs(x):
    visited[x] = True
    
    for i in arr[x]:
        if not visited[i]:
            dfs(i)
            

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)