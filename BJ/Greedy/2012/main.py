import sys
input = sys.stdin.readline

n = int(input())
s = sorted([int(input()) for _ in range(n)])
c, r = 1, 0
for i in range(n):
    r += abs(s[i] - c)
    c += 1
print(r)