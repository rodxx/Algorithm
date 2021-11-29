import sys
input = sys.stdin.readline

n = int(input())
s = [float(input()) for _ in range(n)]
d = [0.0]*n
d[0] = s[0]
for i in range(1, n):
    d[i] = max(s[i], s[i]*d[i-1])
print("%.3f"%max(d))