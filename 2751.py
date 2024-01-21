# 2751

import sys

n = int(input())
score = []

for i in range(n):
    score.append(int(sys.stdin.readline()))

score.sort()

for i in score:
    print(i)