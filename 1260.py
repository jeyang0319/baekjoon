# 1260

from collections import deque

n, m, v = map(int, input().split())

matrix = [[0] * (n + 1) for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visitied):
    visited[i] = True
    print(i, end = ' ')
    for c in range(len(matrix[i])):
        if matrix[i][c] == 1 and not visited[c]:
            dfs(matrix, c, visitied)
            
def bfs(matrix, i, visitied):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visitied[value]:
            print(value, end=' ')
            visitied[value] = True
            for c in range(len(matrix[value])):
                if matrix[value][c] == 1 and not visitied[c]:
                    queue.append(c)

dfs(matrix, v, visited)
visitied = [False] * (n+1)
print()
bfs(matrix, v, visitied)