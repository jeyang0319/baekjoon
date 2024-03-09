# 2667

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
graph = []
s = []
global cnt
cnt = 1

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            global cnt
            cnt += 1
            dfs(nx, ny)

for _ in range(n):
    l = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(l)
    
    
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x, y)
            s.append(cnt)
            cnt = 1

s.sort()
print(len(s))
for i in s:
    print(i)