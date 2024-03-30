# 15651

import sys

n, m = map(int, sys.stdin.readline().split())
lst = []

def back():
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(1, n+1):
        lst.append(i)
        back()
        lst.pop()
        
back()