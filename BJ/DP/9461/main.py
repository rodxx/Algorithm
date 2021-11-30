import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    d = [0]*101
    d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
    for i in range(6, n+1):
        d[i] = d[i-5] + d[i-1]
    print(d[n])