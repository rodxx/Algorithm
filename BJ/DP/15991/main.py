import sys
input = sys.stdin.readline
t = 10**9+9

d = [1,1,2,2]+[0]*(10**5)

for i in range(4, 10**5+1):
    for k in range(1,4):
        if i-2*k >= 0:
            d[i] += d[i-2*k] % t

for _ in range(int(input())):
    n = int(input())
    print(d[n] % t)