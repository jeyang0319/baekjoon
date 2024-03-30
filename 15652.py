# 15652

import sys

n, m = map(int, sys.stdin.readline().split())
lst = []

def back(s):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(s, n+1):
        lst.append(i)
        back(i)
        lst.pop()
        
back(1)