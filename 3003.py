# 3003

p = [1, 1, 2, 2, 2, 8]

c = list(map(int, input().split()))

for i in range(len(c)):
    print(p[i] - c[i], end=' ')