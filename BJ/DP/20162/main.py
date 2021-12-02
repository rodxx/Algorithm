import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
d = s[:]
for i in range(1, n):
    for j in range(i):
        if s[i] > s[j] and d[i] < d[j] + s[i]:
            d[i] = d[j] + s[i]
print(max(d))