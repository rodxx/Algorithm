import sys
input = sys.stdin.readline

k, i, s = 0, 0, []
n = int(input())
while k <= n:
    i += 1
    k += i*(i+1)//2
    s.append(k)

d = [0] + [300001]*n
for i in range(1, n+1):
    for j in s:
        if j <= i and d[i] > 1+d[i-j]:
            d[i] = 1+d[i-j]
print(d[n])