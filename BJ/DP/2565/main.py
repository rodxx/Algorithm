import sys
input = sys.stdin.readline

n = int(input())
s = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
d = [1]*n
for i in range(1, n):
    for j in range(i):
        if s[j][1] < s[i][1]:
            d[i] = max(d[i], 1+d[j])
print(n - max(d))