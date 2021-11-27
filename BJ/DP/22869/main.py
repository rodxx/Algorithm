import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
d = [False]*(n+1)
d[1] = True
for i in range(2, n+1):
    for j in range(1, i):
        if (i - j)*(1 + abs(s[i] - s[j])) <= k and d[j]:
            d[i] = True
            break
if d[n]:
    print("YES")
else:
    print("NO")