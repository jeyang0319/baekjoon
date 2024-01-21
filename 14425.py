import sys

n, m = map(int, input().split())
s = []
cnt = 0
for i in range(n):
    s.append(sys.stdin.readline().rstrip())
    
for i in range(m):
    string = sys.stdin.readline().rstrip()
    if string in s:
        cnt += 1
        
print(cnt)