# 2346

import sys
from collections import deque

n = int(input())

# enumerate를 사용하면 입력한 값 앞에 인덱스 번호를 붙여서 tuple 형태로 바꿔줌
lst = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while lst:
    idx, i = lst.popleft()
    ans.append(idx + 1)
    if i > 0:
        lst.rotate(-(i-1))
    else:
        lst.rotate(-i)

for j in ans:
    print(j, end= ' ')