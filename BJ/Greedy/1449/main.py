import sys
n, tape = map(int, sys.stdin.readline().rstrip().split())
pipe = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0;start, end = 0, 0;pipe.sort()
while start < n and end < n:
  if pipe[end] - pipe[start] + 1 < tape:
    end += 1
  elif pipe[end] - pipe[start] + 1 == tape:
    end += 1
    start = end
    cnt += 1
  else:
    start=end
    cnt += 1
if start != end:
  cnt += 1
print(cnt)