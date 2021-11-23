import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [0]*n
for i in range(n):
    if d[i-1] < 0:
        d[i] = s[i]
        continue
    d[i] = d[i-1] + s[i]
print(max(d))