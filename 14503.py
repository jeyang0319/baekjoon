# 14503

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
lst = []
visited = [[0] * m for _ in range(n)]
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    lst.append(l)
cnt = 0

def bfs(i, j, d):
    global cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt += 1
    # print("i ", i, ", j ", j, ", cnt ", cnt)
    
    while q:
        x, y = q.popleft()
        # print("x ", x, ", y ", y)
        flag = 0
        for _ in range(4):
            d = (d-1) % 4
            
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or lst[nx][ny] == 1:
                continue
            else:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    # print("nx ", nx, ", ny ", ny, ", cnt ", cnt)
                    q.append((nx, ny))
                    flag += 1
                    break
        
        if flag == 0:
            nx = x - dx[d]
            ny = y - dy[d]
            if lst[nx][ny] != 1:
                q.append((nx, ny))
            else:
                print(cnt)
                break
bfs(r, c, d)