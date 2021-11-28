import sys
n = int(sys.stdin.readline().rstrip())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
grow = list(map(int, sys.stdin.readline().rstrip().split()))
result = sum(tree)
grow.sort()
for i in range(n):result += i*grow[i]
print(result)