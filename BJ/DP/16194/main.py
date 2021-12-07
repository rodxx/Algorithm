import sys
input = sys.stdin.readline

n = int(input())
d = [0] + list(map(int, input().split()))
for i in range(2, n+1):
    for j in range(1, i//2+1):
        d[i] = min(d[i], d[j] + d[i-j])
print(d[n])