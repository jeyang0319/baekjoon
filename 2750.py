# 2750

num = int(input())
a = []
for i in range(num):
    n = int(input())
    a.append(n)
    
a.sort()

for i in range(num):
    print(a[i])