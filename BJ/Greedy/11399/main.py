n = int(input());result=0
atm = sorted(list(map(int, input().split())))
for i in range(n):result += sum(atm[:i+1])
print(result)