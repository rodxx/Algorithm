import sys
input = sys.stdin.readline

n = int(input())
s = ' '+input().rstrip()
t = 10**6
d = [t]*(n+1)
d[1] = 0
boj = {'O': 'B', 'J': 'O', 'B': 'J'}
for i in range(2, n+1):
    for j in range(1, i):
        if boj[s[i]] == s[j] and d[j] < t:
            d[i] = min(d[i], d[j]+(i-j)**2)
if d[n] < t:
    print(d[n])
else:
    print(-1)