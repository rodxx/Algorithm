import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().rstrip()))
d = [s[0]]

for i in range(1, n):
    while d and s[i] > d[-1] and k > 0:
        d.pop()
        k -= 1
    d.append(s[i])
print(*d[:len(d)-k], sep='')