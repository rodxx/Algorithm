n = int(input());result = input()
list = [result[0]]
for i in range(1, n):
  l = len(list)
  if list[l - 1] != result[i] : list.append(result[i])
print(min(list.count('R'), list.count('B'))+1)