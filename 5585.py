# 5585
import sys

coin = [500, 100, 50, 10, 5, 1]
n = 1000 - int(sys.stdin.readline())

cnt = 0
for i in coin:
    if i <= n:
        cnt += n//i
        n %= i

print(cnt)