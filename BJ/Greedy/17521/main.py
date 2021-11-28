n, w = map(int, input().split());
price = [1000001] + [int(input()) for _ in range(n)] + [0]
coin = 0
for i in range(1, n+1):
  if price[i-1] >= price[i] <= price[i+1] : coin += w // price[i]; w = w % price[i]
  if price[i-1] <= price[i] >= price[i+1] : w += coin * price[i]; coin = 0
print(w)