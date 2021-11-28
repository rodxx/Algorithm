n, k = map(int, input().split());
if sum(range(1,k+1)) > n:print(-1)
else:
  n -= sum(range(1,k+1))
  if n % k == 0: print(k-1)
  else: print(k)