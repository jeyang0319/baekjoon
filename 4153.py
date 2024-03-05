# 4153

import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if sum(a)== 0:
        break
    
    if a[0]**2 + a[1]**2 == a[2]**2:
        print("right")
    else:
        print("wrong")
