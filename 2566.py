# 2566

a = []

for i in range(9):
    row = list(map(int, input().split()))
    a.append(row)
    
max = -1
max_row = -1
max_col = -1
for row in range(9):
    for col in range(9):
        if a[row][col] > max:
            max = a[row][col]
            max_row = row + 1
            max_col = col + 1

print(max)
print(max_row, max_col)