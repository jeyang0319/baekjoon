# 10989

import sys

num = int(input())

count = [0] * 10001

for i in range(num):
    idx = int(sys.stdin.readline().strip())
    count[idx] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)