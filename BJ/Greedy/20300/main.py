n = int(input())
list = list(map(int, input().split()))
list.sort();max_value = 0
len = (n//2)*2
tmp = list[:len]
for i in range(len//2):
  result = tmp[i] + tmp[-(i+1)]
  max_value = max(result, max_value)
print(max(max_value,list[n-1]))