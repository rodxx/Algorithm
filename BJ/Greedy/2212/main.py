import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
s = sorted(list(map(int, input().split())))
d = sorted([(s[i]-s[i-1]) for i in range(1, n)])
if k >= n:
    r = 0
else:
    r = sum(d[:n-k])
print(r)