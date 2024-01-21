# 2563

num = int(input())

result = 0

paper = [[0] * 101 for _ in range(101)]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

for k in paper:
    result += k.count(1)

print(result)