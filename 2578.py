# 2578

import sys

board = [[0] * 5 for _ in range(5)] ## 빙고판
bx = [0, 1, 2, 3, 4]
by = [0, 1, 2, 3, 4]
dic = {}
for i in range(5):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        dic[l[j]] = (i, j)

q = []
for _ in range(5):
    a, b, c, d, e = map(int, sys.stdin.readline().split())
    q.append(a)
    q.append(b)
    q.append(c)
    q.append(d)
    q.append(e)
check1 = 0
check2 = 0
bingo = 0
idx = -1
while bingo < 3:
    idx += 1
    a, b = dic[q[idx]]
    
    board[a][b] = 1
    # print(board)
    
    for x in bx:
        if sum(board[x]) == 5:
            bx.remove(x)
            bingo += 1
            # print(idx)
            # print("1", board)
            break
    
    for col in by:
        cnt = 0
        for row in range(5):
            cnt += board[row][col]
        if cnt == 5:
            bingo += 1
            # print(idx)
            # print("2", board)
            by.remove(col)
            break
    if check1 == 0:
        if board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] == 5:
            bingo += 1
            # print(idx)
            # print("3", board)
            check1 += 1
    if check2 == 0:
        if board[4][0] + board[3][1] + board[2][2] + board[1][3] + board[0][4] == 5:
            bingo += 1
            # print(idx)
            # print("4", board)
            check2 += 1
    

print(idx+1)