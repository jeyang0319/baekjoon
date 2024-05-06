# 2583
import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, sys.stdin.readline().split())
ans = []
area = [[0] * m for _ in range(n)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1

def dfs(x, y):
    global cnt
    cnt += 1
    area[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if area[nx][ny] == 0:
            area[nx][ny] = 1
            dfs(nx, ny)
            
for x in range(n):
    for y in range(m):
        if area[x][y] == 0:
            cnt = 0
            dfs(x, y)
            ans.append(cnt)
            
ans.sort()
print(len(ans))
print(*ans)