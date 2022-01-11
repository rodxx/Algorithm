import sys
import heapq
input = sys.stdin.readline

s = [int(input()) for _ in range(int(input()))]
heapq.heapify(s)
r = 0

while len(s) > 1:
    a, b = heapq.heappop(s), heapq.heappop(s)
    r += a+b
    heapq.heappush(s, a+b)
print(r)