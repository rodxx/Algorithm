import sys
input = sys.stdin.readline

n = int(input())
s = sorted([tuple(map(int, input().split())) for _ in range(n)])
p = [s[0][1]]
for i in range(1, n):
    p.append(p[i-1] + s[i][1])

for i in range(n):
    if p[-1] - p[i] <= p[i]:
        print(s[i][0])
        break