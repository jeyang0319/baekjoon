# 1181

import sys

n = int(input())
li = []

for i in range(n):
    word = sys.stdin.readline().strip()
    li.append(word)


lst = set(li)
li = list(lst)
li.sort()
li.sort(key=len)

for i in li:
    print(i)