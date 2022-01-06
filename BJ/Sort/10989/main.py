import sys
input = sys.stdin.readline

n = int(input())
s = [0]*10001
for i in range(n):
    s[int(input())] += 1

for i in range(1, 10001):
    for _ in range(s[i]):
        print(i)