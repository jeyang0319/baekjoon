# 2217
import sys

n = int(sys.stdin.readline())
lst= []
for _ in range(n):
    m = int(sys.stdin.readline())
    lst.append(m)

lst.sort(reverse=True)

new = [0] + lst[:]
maximum = 0

for i in range(1, n+1):
    maximum = max(maximum, new[i] * i)

print(maximum)