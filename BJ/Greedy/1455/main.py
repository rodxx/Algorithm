import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
coin = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
count = 0
for i in range(n-1, -1, -1):
  for j in range(m-1, -1, -1):
    if bool(coin[i][j]) :
      count += 1
      for a in range(i+1):
        for b in range(j+1):
          coin[a][b] = 1^coin[a][b]
print(count)