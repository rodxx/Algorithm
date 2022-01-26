import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    r = 0
    heapq.heapify(s)

    while len(s) > 1:
        a, b = heapq.heappop(s), heapq.heappop(s)
        heapq.heappush(s, a+b)
    print(s)