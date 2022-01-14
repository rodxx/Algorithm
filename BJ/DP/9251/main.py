import sys
input = sys.stdin.readline

s1 = ' ' + input().rstrip()
s2 = ' ' + input().rstrip()
d = [[0]*1001 for _ in range(1001)]

l1, l2 = len(s1), len(s2)

for i in range(1, l1):
    for j in range(1, l2):
        if s1[i] == s2[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
print(d[l1-1][l2-1])