import sys
input = sys.stdin.readline

n = int(input())
d = [100001]*(n+1)
d[0] = 0
c = [1, 2, 5, 7]
for i in range(1, n+1):
    for j in c:
        if i-j >= 0:
            d[i] = min(d[i], 1+d[i-j])
print(d[n])