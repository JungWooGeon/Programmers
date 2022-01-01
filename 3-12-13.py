from itertools import combinations
from collections import deque
import copy

def bfs(graph, x_start, y_start, visited):
    queue = deque([(x_start, y_start, 0)])
    visited[x_start][y_start] = True
    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, depth = queue.popleft()
        if graph[x][y] == 2:
            return depth
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
                if not visited[nx][ny]:
                    queue.append((nx, ny, depth+1))
                    visited[nx][ny] = True

    return 0



n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

chicken = []
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 2:
            chicken.append((i, j))

data = list(combinations(chicken, len(chicken) - m))

result = int(1e9)
for cases in data:
    graph_copy = copy.deepcopy(graph)
    for case in cases:
        graph_copy[case[0]][case[1]] = 0
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                visited = [[False]*(n) for _ in range(n)]
                count += bfs(graph_copy, i, j, visited)
    result = min(result, count)

print(result)



