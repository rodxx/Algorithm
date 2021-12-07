import sys
input = sys.stdin.readline
t = 10**9+9
d = [[1,0]]+[[0,0] for _ in range(10**5)]
for i in range(1, 10**5+1):
    for k in range(1, 4):
        if i-k >= 0:
            d[i][0] += d[i-k][1] % t
            d[i][1] += d[i-k][0] % t

for _ in range(int(input())):
    n = int(input())
    print(d[n][1] % t, d[n][0] % t)