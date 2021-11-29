import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    d = [[0, 0] for _ in range(41)]
    d[0], d[1] = [1,0], [0,1]
    for i in range(2, n+1):
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]
    print(*d[n], sep=' ')