import sys
input = sys.stdin.readline

def sol(i):

    if d[i][1] >= 0:
        return d[i][0], d[i][1]

    r, h = [], 0
    for j in range(1, n+1):
        if b[i][0] < b[j][0] and b[i][2] < b[j][2]:
            a, v = sol(j)
            if h < b[j][1] + v:
                r = [j] + a
                h = b[j][1] + v

    d[i][0] = r
    d[i][1] = h

    return r, h

n = int(input())
b = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[[], -1] for _ in range(n+1)]
v1, v2 = sol(0)
print(len(v1), *v1, sep='\n')
