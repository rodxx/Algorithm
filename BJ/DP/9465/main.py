import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    d = [[0]*n for _ in range(2)]

    for c in range(n):
        for r in range(2):
            dr = [(-1)**r, 0, (-1)**r]
            dc = [-1, -2, -2]
            for k in range(3):
                if c+dc[k] < 0:
                    continue
                d[r][c] = max(d[r][c], d[r+dr[k]][c+dc[k]])
            d[r][c] += s[r][c]

    print(max(d[0][n-1], d[1][n-1]))