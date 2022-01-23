import sys
import heapq
input = sys.stdin.readline

n = int(input())
s = sorted([tuple(map(int, input().split())) for _ in range(n)])
q = [s[0][1]]
for i in range(1, n):
    if s[i][0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, s[i][1])
print(len(q))