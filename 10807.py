# 10807

import sys

n = int(sys.stdin.readline())

lst = list(sys.stdin.readline().split())

v = str(sys.stdin.readline().rstrip())
cnt = 0
for i in lst:
    if i == v:
        cnt += 1

print(cnt)