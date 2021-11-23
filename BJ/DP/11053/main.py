import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [1]*n
for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            d[i] = max(d[j] + 1, d[i])
print(max(d))