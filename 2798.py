# 2798

import sys

n, m = map(int, input().split())

num = list(map(int, sys.stdin.readline().split()))

ans = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_lst = num[i] + num[j] + num[k]
            if sum_lst <= m:
                ans.append(sum_lst)

print(max(ans))