import sys
input = sys.stdin.readline

n = int(input())
d = [100001]*(n+1)
d[1] = 1
for i in range(2, n+1):
    if i**(0.5) == int(i**(0.5)):
        d[i] = 1
        continue
    for j in range(1, int(i**(0.5))+1):
        d[i] = min(d[i], 1+d[i-j**2])
print(d[n])