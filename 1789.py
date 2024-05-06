# 1789
import sys

n = int(sys.stdin.readline())

cnt = 0
i = 1
while n >= 0:
    n -= i
    i += 1
    cnt += 1


print(cnt-1)