# 1018

n, m = map(int, input().split())

board = []

for i in range(n):
    lst = list(map(str, input().rstrip()))
    board.append(lst)
    
# 정상적인 체스판 2개 만들기
w = "WB" * 4
b = "BW" * 4

startW = []
startB = []

for i in range(8):
    if i % 2 == 0:
        startW.append(w)
        startB.append(b)
    else:
        startW.append(b)
        startB.append(w)
        
cnt = 64

for i in range(n-7):
    for j in range(m-7):
        sw = 0
        sb = 0
        
        for k in range(8):
            for l in range(8):
                sw += int(board[i + k][j + l] != startW[k][l])
                
                sb += int(board[i + k][j + l] != startB[k][l])
        
        cnt = min(cnt, sw, sb)
        
        if cnt == 0:
            break
        
print(cnt)