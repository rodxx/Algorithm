n = int(input())
before = list(map(int, input())) + [0]
after = list(map(int, input())) + [0]

def zero_switch_off(list):
  count = 0
  for i in range(1, n):
    if list[i-1] != after[i-1]:
      count += 1
      for j in range(-1,2):list[i+j] = 1^list[i+j]
  if list[n-1] != after[n-1]: return -1
  return count

def zero_switch_on(list):
  count = 1
  list[0] = 1^list[0]
  list[1] = 1^list[1]
  for i in range(1, n):
    if list[i-1] != after[i-1]:
      count += 1
      for j in range(-1,2):list[i+j] = 1^list[i+j]
  if list[n-1] != after[n-1]: return -1
  return count

result1, result2 = zero_switch_off(before[:]), zero_switch_on(before[:])
if min(result1, result2) != -1 : print(min(result1, result2))
else : print(max(result1, result2))

