# 10816

import sys

n = int(input())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

m = int(input())
test = list(map(int, sys.stdin.readline().split()))


cnt = {}
for i in num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for j in test:
    if j in cnt:
        print(cnt[j], end = ' ')
    else:
        print(0, end = ' ')