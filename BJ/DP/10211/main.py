import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    d = [0]*n
    d[0] = s[0]

    for i in range(1, n):
        if d[i-1] < 0:
            d[i] = s[i]
            continue
        d[i] = d[i-1]+s[i]
    print(max(d))