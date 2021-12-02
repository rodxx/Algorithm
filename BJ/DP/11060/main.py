import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [10**3]*n
d[0] = 0
for i in range(1, n):
    for j in range(i):
        if i <= j + s[j]:
            d[i] = min(d[i], d[j]+1)
if d[n-1] < 10**3:
    print(d[n-1])
else:
    print(-1)