# 11050
import math
n, k = map(int, input().split())

a = 1
for i in range(k):
    a *= n - i
    
print(a // (math.factorial(k)))