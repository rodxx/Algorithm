import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
  box = []; cnt = 0; result = 0
  j, n = map(int, input().rstrip().split())
  for _ in range(n):
    a, b = map(int, input().rstrip().split())
    box.append(a*b)
  box.sort(reverse=True)
  for i in range(n):
    if j > result : result += box[i]
    if j <= result : cnt = i + 1; break
  print(cnt)