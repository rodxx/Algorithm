import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    age, name = input().split()
    s.append((int(age), name))
s.sort(key=lambda x: x[0])

for a, b in s:
    print(a, b)