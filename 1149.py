# 1149
import sys

n = int(sys.stdin.readline())
color = []

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    color.append(lst)

for i in range(1, n):
    color[i][0] += min(color[i-1][1], color[i-1][2])
    color[i][1] += min(color[i-1][0], color[i-1][2])
    color[i][2] += min(color[i-1][0], color[i-1][1])

print(min(color[n-1]))