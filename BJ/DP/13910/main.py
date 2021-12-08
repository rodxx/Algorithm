import sys
input = sys.stdin.readline

n, m = map(int, (input().split()))
s = list(map(int, input().split()))
d = [10**4+1]*10001
d[0] = 0
for i in range(m):
    for j in range(i+1, m):
        if s[i] + s[j] <= 10**4:
            s.append(s[i]+s[j])

for i in range(1, n+1):
    for j in s:
        if i-j >= 0 and d[i] > d[i-j]+1:
            d[i] = d[i-j]+1

if d[n] < 10**4+1:
    print(d[n])
else:
    print(-1)