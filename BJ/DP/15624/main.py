import sys
input = sys.stdin.readline

n = int(input())
d = [0, 1]
cnt = 0
for i in range(2, n+1):
    d[cnt] = (d[cnt] + d[cnt^1]) % (10**9+7)
    cnt ^= 1
print(d[n%2])