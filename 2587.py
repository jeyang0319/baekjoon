# 2587
sum = 0
a = []
for i in range(5):
    num = int(input())
    sum += num
    a.append(num)

a.sort()
median = a[2]
mean = int(sum / 5)

print(mean)
print(median)