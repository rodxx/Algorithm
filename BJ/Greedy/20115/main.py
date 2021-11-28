n = int(input())
drink = list(map(int, input().split()))
drink.sort();result=0
for i in drink:result += i/2
result += drink[n-1]/2
print(result)