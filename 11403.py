11403

import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
    

path = graph
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                path[i][j] = 1

for i in range(n):
    for j in range(n):
        if j == (n-1):
            print(path[i][j])
        else:
            print(path[i][j], end =' ')