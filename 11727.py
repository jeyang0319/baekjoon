# 11727
import sys

n = int(sys.stdin.readline())

arr = [0] * (n+1)
arr[0] = 1
arr[1] = 3


for i in range(2, n+1):
    arr[i] = arr[i-2] * 2 + arr[i-1]
print(arr[n-1]%10007)