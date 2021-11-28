s = input()
count_m = 0
result_max = ''
result_min = ''
for i in range(len(s)):
  if s[i] == 'K':
    result_max += '5' + '0'*count_m
    count_m = 0
  else:
    count_m += 1

result_max += '1'*count_m

count_m = 0
for i in range(len(s)):
  if s[i] == 'K':
    if count_m > 0 :
      result_min += '1' + '0'*(count_m - 1)
      count_m = 0
    result_min += '5'
  else:
    count_m += 1

if count_m > 0 :
  result_min += '1' + '0'*(count_m - 1)

print(result_max)
print(result_min)