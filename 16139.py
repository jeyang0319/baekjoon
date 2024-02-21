# 16139

import sys

s = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline().rstrip())
lst = []

dic = {}

for i in range(n):
    q = list(sys.stdin.readline().split())
    if q[0] not in dic:
        dic[q[0]] = 1
    else:
        dic[q[0]] += 1

print(dic)
