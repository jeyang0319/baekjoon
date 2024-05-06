# 4963

import sys
from collections import deque

network = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            
            if network[nx][ny] == 1:
                network[nx][ny] = 0
                q.append((nx, ny))
            

while True:
    network = []
    h, w = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    for _ in range(w):
        lst = list(map(int, sys.stdin.readline().split()))
        network.append(lst)
    cnt = 0
    for x in range(w):
        for y in range(h):
            if network[x][y] == 1:
                network[x][y] = 0
                bfs(x, y)
                cnt += 1
    
    print(cnt)