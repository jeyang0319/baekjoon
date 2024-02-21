# 2559

import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sum_list = []
sum = 0

for i in range(k):
    sum += lst[i]

max_sum = sum

for j in range(n-k):
    sum = sum - lst[j] + lst[j+k]
    if max_sum < sum :
        max_sum = sum
print(max_sum)
