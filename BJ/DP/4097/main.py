import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n:
        break
    s = [int(input()) for _ in range(n)]
    d = [s[0]]+[0]*(n-1)
    for i in range(1, n):
        d[i] = s[i]
        if d[i-1] > 0:
            d[i] += d[i-1]
    print(max(d))