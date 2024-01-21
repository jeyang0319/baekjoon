# 25305

num, cut = map(int, input().split())
a = []

score = list(map(int, input().split()))

score.sort(reverse=True)
print(score[cut-1])