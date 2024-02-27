# 1931

import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a,b])
    

lst.sort(key= lambda x:(x[1], x[0]))

a = 0
cnt = 0
for i in lst:
    start, end = i
    if start >= a:
        cnt += 1
        a = end

print(cnt)