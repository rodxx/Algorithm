import sys
n = int(sys.stdin.readline().rstrip())
rope = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
rope.sort(reverse=True); result = 0
for i in range(n):
  result = max((i+1)*rope[i], result)
print(result)