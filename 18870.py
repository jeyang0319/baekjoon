# 18870

import sys

n = int(input())

lst = list(map(int, sys.stdin.readline().split()))
li = set(lst)
li = sorted(list(li))
dic = {}
for i in range(len(li)):
    dic[li[i]] = i
    
for j in range(len(lst)):
    print(dic[lst[j]], end = ' ')