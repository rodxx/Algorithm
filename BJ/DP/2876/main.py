import sys
input = sys.stdin.readline

n = int(input())
s = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]
d = [[0]*6 for _ in range(n+1)]
r = []
for i in range(1, n+1):
    g1, g2 = s[i][0], s[i][1]
    d[i][g1] = d[i-1][g1] + 1
    d[i][g2] = d[i-1][g2] + 1
    if d[i][g1] > d[i][g2]:
        r.append((d[i][g1], g1))
    elif d[i][g1] == d[i][g2]:
        r.append((d[i][g1], min(g1, g2)))
    else:
        r.append((d[i][g2], g2))
r = sorted(sorted(r, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)
print(r[0][0], r[0][1])