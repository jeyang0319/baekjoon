# 15650

import sys

n, m = map(int, sys.stdin.readline().split())
ans = []

def back(s):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(s, n+1):
        if i not in ans:
            ans.append(i)
            back(i+1)
            ans.pop()

back(1)