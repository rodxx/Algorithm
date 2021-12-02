import sys
input = sys.stdin.readline

n = int(input())
d = [0, 1, 2, 4, 7]+[0]*16
for i in range(5, n+1):
    d[i] = d[i-1]*2
    if i % 2 == 0:
        d[i] -= (d[i-4]+d[i-5])
print(d[n])