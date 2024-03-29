import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

t = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = []
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF]*n for _ in range(n)]
    x, y = 0, 0
    q = [(graph[x][y], x, y)]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    result.append(distance[n-1][n-1])

for x in result:
    print(x)