#1932
import sys

n = int(sys.stdin.readline())

arr = [[0] * n for _ in range(n)]
num = int(sys.stdin.readline())
arr[0][0] = num
for i in range(1, n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr[i][:i+1] = lst[:]
    
dp = [[0] * n for _ in range(n)]
dp[0][0] = num
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] += max(dp[i-1][j] + arr[i][j], dp[i-1][j-1] + arr[i][j])

print(max(dp[n-1]))