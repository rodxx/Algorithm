import sys
input = sys.stdin.readline
n ,l = map(int, input().rstrip().split())
list = sorted(list(map(int, input().rstrip().split())))
for i in list:
  if i <= l: l += 1
print(l)