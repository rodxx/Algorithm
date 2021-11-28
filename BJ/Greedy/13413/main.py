from sys import stdin as s
result = []
for _ in range(int(s.readline().rstrip())):
  n = int(s.readline().rstrip())
  cnt = 0; w_cnt = 0;b_cnt = 0
  before = list(s.readline().rstrip())
  after = list(s.readline().rstrip())
  for i in range(n):
    if before[i] != after[i]:
      if before[i] == 'W': w_cnt += 1
      else : b_cnt += 1
  if w_cnt == b_cnt : cnt += w_cnt
  else:cnt += max(w_cnt, b_cnt)
  result.append(cnt)
for i in result:print(i)