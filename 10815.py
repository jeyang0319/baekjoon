# 10815

import sys

n = int(input()) # 상근이가 갖고 있는 숫자 n개

n_set = set(map(int, sys.stdin.readline().split()))

m = int(input())

m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if i in n_set:
        print(1, end=' ')
    else:
        print(0, end=' ')