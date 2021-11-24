import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [0]*n
for i in range(n):
    d[i] = s[i]
    for j in range(i):
        if s[i] > s[j]:
            d[i] = max(d[i], d[j] + s[i])
print(max(d))