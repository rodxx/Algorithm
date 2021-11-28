import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
count = 0; state = 0
for i in range(n):
  for j in range(m):
    if A[i][j] != B[i][j]:
      if i+2 >= n or j+2 >= m :
        state=1
        break
      count += 1
      for a in range(3):
        for b in range(3):
          A[i+a][j+b] = 1^A[i+a][j+b]
if state == 0 : print(count)
else : print(-1)