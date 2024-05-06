# 2468

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
area = []
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    area.append(l)
    
max_num = max(max(area))
lst = []

def dfs(network, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if network[nx][ny] == 1:
            network[nx][ny] = 0
            dfs(network, nx, ny)
            

def problem(num):
    ans = 0
    network = [row[:] for row in area]
    for x in range(n):
        for y in range(n):
            if network[x][y] <= num:
                network[x][y] = 0
            else:
                network[x][y] = 1
    
    for x in range(n):
        for y in range(n):
            if network[x][y] == 1:
                network[x][y] = 0
                dfs(network, x, y)
                ans += 1
        lst.append(ans)
    return max(lst)

answer = 0
for i in range(2, max_num):
    answer = max(answer, problem)
