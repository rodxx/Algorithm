import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)

def sol(x):
    if x == n:
        return 1

    if d[x] >= 0:
        return d[x]

    d[x] = 0
    for i in range(x, n):
        v = int(s[x:i+1])
        if v > 26:
            break
        elif v == 0:
            return 0
        else:
            d[x] += sol(i+1)

    return d[x]

s = input().rstrip()
n = len(s)
d = [-1]*n
print(sol(0) % 10**6)