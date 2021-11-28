n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))
min_price = oil[0]
result = 0
for i in range(1,n):
  result += distance[i-1] * min_price
  if oil[i] < min_price :
    min_price = oil[i]
print(result)