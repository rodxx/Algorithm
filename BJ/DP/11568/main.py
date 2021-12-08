import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [s[0]]
for i in range(1, n):
    if d[-1] < s[i]:
        d.append(s[i])
    else:
        d[bisect_left(d, s[i])] = s[i]
print(len(d))