import sys
n = int(sys.stdin.readline().rstrip())
tree = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
sum = 0
for i in tree:
  count += i // 2
  sum += i

if sum % 3 != 0:
  print('NO')
else:
  total = sum // 3
  if count >= total:
    print('YES')
  else:
    print('NO')