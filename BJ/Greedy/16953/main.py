a, b = map(int, input().split())
count = 0
result = b

while result > a :

  if (result-1) % 10 == 0 :
    result = (result - 1)//10
    count += 1
  elif result % 2 == 0 :
    result //= 2
    count += 1
  else:
    break

if result == a:
  print(count+1)
else:
  print(-1)