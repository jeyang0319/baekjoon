# 11660

import sys

n, m = map(int, sys.stdin.readline().split())

table = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    a = list(map(int, sys.stdin.readline().split()))
    sum = 0
    j = 1
    for num in a:
        sum += num
        table[i][j] = sum
        j += 1

    
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = 0
    sum = 0
    for i in range(x1, x2+1):
        sum += (table[i][y2] - table[i][y1-1])
        
    print(sum)
    