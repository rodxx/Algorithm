result = []
s = input()
for i in range(len(s)):
  if i == 0 : result.append(s[i])
  elif result[-1] != s[i] : result.append(s[i])
print(min(result.count('1'), result.count('0')))