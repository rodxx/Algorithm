import sys
input = sys.stdin.readline

d = [[0,0,0] for _ in range(10**5+1)]
d[1], d[2], d[3] = [1,0,0], [0,1,0], [1,1,1]
k = 10**9+9
for i in range(4, 10**5+1):
    d[i][0] = (d[i - 1][1] + d[i - 1][2]) % k
    d[i][1] = (d[i - 2][0] + d[i - 2][2]) % k
    d[i][2] = (d[i - 3][0] + d[i - 3][1]) % k
for _ in range(int(input())):
    n = int(input())
    print(sum(d[n]) % k)