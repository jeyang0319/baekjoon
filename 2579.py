# 2579

import sys

n = int(sys.stdin.readline())
step = [0] * 300

for i in range(n):
    step[i] = int(sys.stdin.readline())


dp = [0] * 300

dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0] + step[2], step[1] + step[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[n-1])