# 7562

import sys
from collections import deque

n = int(sys.stdin.readline())

def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            return (graph[x][y])
        
        visited[x][y] = True
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            
            if nx == a and ny == b:
                return (graph[nx][ny])

for _ in range(n):
    l = int(sys.stdin.readline())
    ax, ay = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    
    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    print(bfs(ax, ay))

