# 10798

a = []
ans = ''
word_len = 0
for i in range(5):
    word = list(map(str, input()))
    if len(word) > word_len:
        word_len = len(word)
    a.append(word)

for col in range(word_len):
    for row in range(5):
        try:
            ans += a[row][col]
        except:
            pass
        
print(ans)