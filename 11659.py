# 11659

import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

sum_list = [0]
sum = 0
for i in lst:
    sum += i
    sum_list.append(sum)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ans = sum_list[b] - sum_list[a-1]
    print(ans)