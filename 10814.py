# 10814

import sys

n = int(input())
li = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    li.append([age, name])

li.sort(key = lambda x: x[0])

for i in li:
    print(i[0], i[1])