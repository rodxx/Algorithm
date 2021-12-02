import sys
input = sys.stdin.readline

d = [0]*(10**6+1)
d[1], d[2], d[3] = 1, 2, 4
k = 10**9 + 9
for i in range(4, 10**6+1):
    d[i] = d[i-1] % k + d[i-2] % k + d[i-3] % k

for _ in range(int(input())):
    n = int(input())
    print(d[n] % k)