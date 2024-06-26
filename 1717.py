# 1717

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(m):
    q, a, b = map(int, sys.stdin.readline().split())
    
    if q == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")