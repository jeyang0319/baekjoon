# 11726

import sys

n = int(sys.stdin.readline())

arr = [0] * 1000
arr[0] = 1
arr[1] = 2

for i in range(2, 1000):
    arr[i] = arr[i-2] + arr[i-1]


print(arr[n-1]%10007)