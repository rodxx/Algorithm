import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
s = sorted([tuple(map(int, input().split())) for _ in range(n)])

for i in s:
    heapq.heappush(q, i[1])
    while len(q) > i[0]:
        heapq.heappop(q)
print(sum(q))