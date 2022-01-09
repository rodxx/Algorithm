import sys
input = sys.stdin.readline

n = int(input())
s = sorted([int(input()) for _ in range(n)])
print(*s, sep="\n")