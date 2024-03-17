# 2003

import sys

n, m = map(int, sys.stdin.readline().split())

lst = [0]

a = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in a:
    sum += i
    lst.append(sum)
    
cnt = 0

for i in range(n+1):
    if lst[i] == m:
        cnt += 1
        continue
    for j in range(i-1, -1, -1):
        if lst[i] - lst[j] > m :
            break
        if lst[i] - lst[j] == m:
            cnt += 1
            break

print(cnt)