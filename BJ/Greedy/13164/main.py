import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
r = sorted([s[i]-s[i-1] for i in range(1, n)], reverse=True)
print(sum(r[k-1:]))