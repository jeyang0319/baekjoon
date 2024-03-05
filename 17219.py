# 17219

import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
    email, pw = map(str, sys.stdin.readline().split())
    dic[email] = pw

for _ in range(m):
    e = sys.stdin.readline().rstrip()
    print(dic[e])