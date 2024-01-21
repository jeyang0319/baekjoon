# 11478

import sys

string = sys.stdin.readline().rstrip()

ans = set()

for i in range(len(string)):
    for j in range(i+1, len(string) + 1):
        ans.add(string[i:j])
        
print(len(ans))