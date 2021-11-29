r, c, w = map(int, input().split())
d = []
for i in range(r+w):
    d.append([0]*(i+2))
d[1][1] = 1

result = 0
for i in range(1, r+w):
    for j in range(1, i+1):
        d[i][j] += d[i-1][j-1] + d[i-1][j]
        if r <= i < r+w and c <= j < c+i-r+1:
            result += d[i][j]
print(result)