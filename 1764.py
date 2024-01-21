# 1764

import sys

n, m = map(int, input().split())
dic = {}

for i in range(n):
    name = sys.stdin.readline().rstrip()
    dic[name] = 1
    

for j in range(m):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
        
ans = []
for i in dic:
    if dic[i] == 2:
        ans.append(i)

ans.sort()

print(len(ans))
for k in ans:
    print(k)