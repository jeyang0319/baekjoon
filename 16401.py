# 16401
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

ans = 0
start = 1
end = max(lst)

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for x in lst:
        if x >= mid:
            cnt += x//mid
    
    if cnt < n:
        end = mid-1
    else:
        ans = mid
        start = mid + 1

print(ans)