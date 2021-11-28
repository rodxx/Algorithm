n = int(input()); result = 0; cnt = 0
stick = sorted(list(map(int, input().split())),reverse=True)
for i in range(n-1):
  cnt += stick[i]
  result += stick[i+1] * cnt
print(result)