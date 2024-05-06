# 1439
import sys

s = sys.stdin.readline().rstrip()

tmp = s[0]

if tmp == '0':
    zero = 1
    one = 0
else:
    zero = 0
    one = 1

for i in s:
    if i != tmp:
        if i == '0':
            zero += 1
            tmp = i
        else:
            one += 1
            tmp = i
    else:
        continue

print(min(zero, one))