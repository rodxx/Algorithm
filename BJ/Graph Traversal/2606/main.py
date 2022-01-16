import sys
from collections import deque
input = sys.stdin.readline

def bfs(g,v,visit):
    visit[v] = True
    queue.append(v)
    while queue:
        k = queue.popleft()
        for i in g[k]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
queue = deque()
for _ in range(int(input())):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(graph,1,visited)
print(visited[2:].count(True))