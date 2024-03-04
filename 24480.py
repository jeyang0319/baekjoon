# 24480

import sys
sys.setrecursionlimit(10**6) # 런타임 에러 방지

n, m, r = map(int, sys.stdin.readline().split())

network = [[] for _ in range(n+1)]
visited = [False] * (n+1)
stack = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)
        
for i in range(n+1):
    network[i].sort(reverse=True)

def dfs(r):
    global cnt
    cnt += 1
    visited[r] = True
    stack[r] = cnt
    for i in network[r]:
        if not visited[i]:
            dfs(i)
    
dfs(r)
for i in range(1, n+1):
    print(stack[i])