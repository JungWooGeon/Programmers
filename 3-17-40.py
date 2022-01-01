import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if not b in graph[a]:
        graph[a].append(b)
    if not a in graph[b]:
        graph[b].append(a)

distance = [INF]*(n+1)

q = []
heapq.heappush(q, (0, 1))

while q:
    distance[1] = 0
    dist, x = heapq.heappop(q)
    if distance[x] < dist:
        continue
    for i in graph[x]:
        cost = dist + 1
        if distance[i] > cost:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

distance[0] = -1
max_index = []
for i in range(1, n+1):
    if distance[i] == max(distance):
        max_index.append(i)

print(min(max_index), max(distance), len(max_index))