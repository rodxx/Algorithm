import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = sorted(list(map(int, input().split())))
print(s[k-1])