import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [1]*n
for i in range(1, n):
    for j in range(i):
        if s[i] < s[j] and d[i] < 1+d[j]:
            d[i] = 1+d[j]
print(n-max(d))