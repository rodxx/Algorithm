import sys
input = sys.stdin.readline

n = int(input())
s = [0]+list(map(int, input().split()))
d1, d2 = [1]*(n+1), [1]*(n+1)
for i in range(2, n+1):
    if s[i-1] <= s[i]:
        d1[i] += d1[i-1]
    if s[i-1] >= s[i]:
        d2[i] += d2[i-1]
print(max(max(d1), max(d2)))