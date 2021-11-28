import sys
n= int(sys.stdin.readline().rstrip())
x_point, y_point = [], []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  x_point.append(x)
  y_point.append(y)
x_point.sort();y_point.sort()
x, y = x_point[n//2], y_point[n//2]
result = 0
for i in range(n):result += abs(x - x_point[i]) + abs(y - y_point[i])
print(result)