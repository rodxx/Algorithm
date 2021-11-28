from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
count = 0
while k > 0 :
  start = bisect_right(coin, k) - 1
  count += k // coin[start]
  k = k % coin[start]
print(count)