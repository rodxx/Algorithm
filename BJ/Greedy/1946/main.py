import sys

t = int(sys.stdin.readline().rstrip())
test = []
for i in range(t):
  n = int(sys.stdin.readline().rstrip())
  array = []
  for j in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    array.append((a, b))

  array.sort()

  count = 1
  highest_rank = array[0][1]
  for j in range(1, n):
    if array[j][1] < highest_rank :
      highest_rank = array[j][1]
      count += 1

  test.append(count)

for i in range(t):
  print(test[i])