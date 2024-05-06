# 1003
import sys

t = int(sys.stdin.readline())
lst = [[0, 0] for _ in range(41)]
lst[0] = [1, 0]
lst[1] = [0, 1]

for i in range(2, 41):
    a = lst[i-1][0] + lst[i-2][0]
    b = lst[i-1][1] + lst[i-2][1]
    lst[i] = [a, b]
    
for _ in range(t):
    n = int(sys.stdin.readline())
    print(*lst[n])