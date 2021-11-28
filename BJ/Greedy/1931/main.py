import sys
n = int(sys.stdin.readline().rstrip())
list = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
list.sort();list = sorted(list, key=lambda x:x[1])
next = 0;count = 0
for i in list:
  if i[0] >= next:
    next = i[1]
    count += 1
print(count)