s =input().split('-')
result = 0
for i in range(len(s)):
  if i != 0:
    result += -sum(map(int, s[i].split('+')))
  else:
    result += sum(map(int, s[i].split('+')))
print(result)