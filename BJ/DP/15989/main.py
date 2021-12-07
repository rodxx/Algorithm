import sys
input = sys.stdin.readline

d = [1] + [0]*10000
for i in range(1, 4):
    for j in range(1, 10001):
        if j-i >= 0:
            d[j] += d[j-i]

for _ in range(int(input())):
    n = int(input())
    print(d[n])