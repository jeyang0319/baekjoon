# 1541

import sys

s = sys.stdin.readline().rstrip()
s = s.split("-")

answer = 0
for i in s[0].split("+"):
    answer += int(i)

for i in range(1, len(s)):
    for j in s[i].split("+"):
        answer -= int(j)

print(answer)