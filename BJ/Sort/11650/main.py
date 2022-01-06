import sys
input = sys.stdin.readline

n = int(input())
s = sorted([tuple(map(int, input().split())) for _ in range(n)])
for x, y in s:
    print(x, y)