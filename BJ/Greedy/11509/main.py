import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
arrow = [0]*(1000000+1)

for i in array:
  if arrow[i] == 0:
    count += 1
    arrow[i-1] += 1
  else:
    arrow[i] -= 1
    arrow[i-1] += 1

print(count)