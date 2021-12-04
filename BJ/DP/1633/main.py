import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3+1)

def sol(i, w, b):
    if i == n:
        return 0

    if d[i][w][b] > 0:
        return d[i][w][b]

    m = sol(i+1, w, b)
    if w+1 <= 15:
        m = max(m, s[i][0] + sol(i+1, w+1, b))
    if b+1 <= 15:
        m = max(m, s[i][1] + sol(i+1, w, b+1))

    d[i][w][b] = m
    return m


s = [[0,0]]
for i in sys.stdin:
    s.append(list(map(int, i.split())))
n = len(s)
d = [[[0]*16 for _ in range(16)] for _ in range(n)]
print(sol(1,0,0))