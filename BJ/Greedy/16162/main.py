from sys import stdin as s
n, a, d = map(int, s.readline().rstrip().split())
pitch = list(map(int, s.readline().rstrip().split()))
cnt = 0
for i in range(n):
  if pitch[i] == a + cnt*d:cnt+=1
print(cnt)