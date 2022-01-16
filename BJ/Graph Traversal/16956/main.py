import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
farm = [list(input().rstrip()) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flag = 0
for i in range(r):
    for j in range(c):
        if farm[i][j] == 'S':
            for k in range(4):
                px, py = i+dx[k], j+dy[k]
                if px < 0 or px > r-1 or py < 0 or py > c-1:
                    continue
                if farm[px][py] == '.':
                    farm[px][py] = 'D'
                elif farm[px][py] == 'W':
                    flag = 1
                    break
    if flag:
        print(0)
        exit(0)

print(1)
for i in range(r):
    print(''.join(farm[i]))