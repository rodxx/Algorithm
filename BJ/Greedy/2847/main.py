from sys import stdin as s
n = int(s.readline().rstrip())
score = [int(s.readline().rstrip()) for _ in range(n)]
cnt = 0
for i in range(n-1,0,-1):
  if score[i] <= score[i-1]:
    cnt += score[i-1] - score[i] + 1
    score[i-1] = score[i] - 1
print(cnt)