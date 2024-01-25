# 25192
import sys

n = int(input())
names = set()
cnt = 0
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name == "ENTER":
        names = set()
    elif name not in names:
        names.add(name)
        cnt += 1
        
print(cnt)