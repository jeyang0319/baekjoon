# 2805

import sys
n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))
s, e = 1, max(tree)

while s <= e:
    mid = (s + e) // 2
    t_sum = 0
    
    for i in tree:
        if i > mid:
            t_sum += i - mid
            
    if t_sum >= m:
        s = mid + 1
    else:
        e = mid - 1
        
print(e)