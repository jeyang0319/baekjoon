# 7576

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
box = []
q = deque()

for _ in range(m):
    lst = list(map(int, sys.stdin.readline().split()))
    box.append(lst)
    

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append([i, j])
            
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

bfs()

def problem():
    ans = 0
    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                return -1
            ans = max(ans, box[i][j]-1)
    
    return ans

print(problem())