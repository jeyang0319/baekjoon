# 7785

import sys

n = int(input())
name_lst = set()

for i in range(n):
    name, status = map(str, sys.stdin.readline().split())
    if status == 'enter':
        name_lst.add(name)
    elif status == 'leave':
        name_lst.remove(name)

ans = list(name_lst)
ans.sort(reverse=True)
for j in ans:
    print(j)