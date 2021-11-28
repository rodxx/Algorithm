n, m = map(int, input().split())
word = []
result = ''
length = 0
for i in range(n):
    words = input()
    length += len(words)
    word.append(words)
length += n - 1
# 단어 사이에 들어가야 하는 언더바 개수 계산
under_count = (1 + (m - length) // (n - 1))
under = [under_count] * n
# 추가로 넣어야 하는 언더바의 개수 계산
bar_count = (m - length) % (n - 1)

for i in range(1, n):
    if bar_count == 0:
        break

    if word[i][0].islower():
        bar_count -= 1
        under[i] += 1

for i in range(n - 1, 0, -1):
    if bar_count == 0:
        break
    if word[i][0].isupper():
        under[i] += 1
        bar_count -= 1

result = word[0]
for i in range(1, n):
    result += '_' * under[i] + word[i]
print(result)