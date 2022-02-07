import sys
input = sys.stdin.readline

def calculate(x, y, d1, d2):
    area = [0, 0, 0, 0, 0]
    for r in range(N):
        for c in range(N):

            if 0 <= r < x+d1 and 0 <= c <= y:
                if r+c < x+y:
                    area[0] += A[r][c]
                else:
                    area[4] += A[r][c]
            elif 0 <= r <= x+d2 and y < c <= N-1:
                if r-c < x-y:
                    area[1] += A[r][c]
                else:
                    area[4] += A[r][c]
            elif x+d1 <= r <= N-1 and 0 <= c < y-d1+d2:
                if r-c > x-y+2*d1:
                    area[2] += A[r][c]
                else:
                    area[4] += A[r][c]
            elif x+d2 < r <= N-1 and y-d1+d2 <= c <= N-1:
                if r+c > x+y+2*d2:
                    area[3] += A[r][c]
                else:
                    area[4] += A[r][c]
            else:
                area[4] += A[r][c]
    return max(area) - min(area)


def divide(a, b):
    m = 2000
    for d1 in range(1, N):
        for d2 in range(1, N):
            if a + d1 + d2 > N-1 or b-d1 < 0 or b+d2 > N-1:
                continue
            m = min(m, calculate(a, b, d1, d2))
    return m

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 2000

for x in range(N):
    for y in range(N):
        ans = min(ans, divide(x, y))
print(ans)