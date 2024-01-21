# 1427
import sys

num = list(str(sys.stdin.readline().strip()))
num.sort(reverse=True)

for i in num:
    print(i, end='')