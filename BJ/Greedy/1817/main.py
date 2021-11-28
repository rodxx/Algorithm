import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
book = list(map(int, input().rstrip().split()))
result = 0; cnt=0
for i in range(n):
  result += book[i]
  if result > m :
    result = book[i]
    cnt += 1
if result <= m and n > 0 : cnt+=1
print(cnt)