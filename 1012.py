# 1012

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= a or ny < 0 or ny >= b:
            continue
        
        if graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(nx, ny)
        

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
        
    graph = [[0]*a for _ in range(b)]

    for _ in range(c):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    answer = 0
    for i in range(a):
        for j in range(b):
            if graph[j][i] == 1:
                dfs(i, j)
                answer += 1
    
    print(answer)