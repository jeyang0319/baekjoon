# 1620

import sys

n, m = map(int, input().split())
name_lst = {}
arr_lst = {}

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    name_lst[i] = name
    arr_lst[name] = i
    
    

for j in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(name_lst[int(q)])
    else:
        print(arr_lst[q])


