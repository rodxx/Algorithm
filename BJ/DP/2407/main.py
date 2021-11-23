import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [1]*(n+1)
for i in range(2,n+1):
    d[i] = d[i-1]*i
print(d[n]//(d[m]*d[n-m]))