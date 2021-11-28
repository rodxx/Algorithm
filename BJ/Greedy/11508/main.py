import sys
n = int(sys.stdin.readline().rstrip())
list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
list.sort(reverse=True)
result=0
for i in range(n):
  if i%3==2:continue
  result += list[i]
print(result)