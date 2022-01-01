from itertools import combinations
import copy

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(graph, x, y, visited):
    visited[x][y] = True
    graph[x][y] = 2
    global n
    global m

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= m-1:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs(graph, nx, ny, visited)



blank = []
infection = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
        if graph[i][j] == 2:
            infection.append([i, j])

candidate = list(combinations(blank, 3))

result = 0

for candi in candidate:
    graph_copy = copy.deepcopy(graph)
    for can in candi:
        graph_copy[can[0]][can[1]] = 1
    
    visited = [[False]*m for _ in range(n)]
    for infect in infection:
        dfs(graph_copy, infect[0], infect[1], visited)

    count = 0
    for a in graph_copy:
        for b in a:
            if b == 0:
                count += 1

    result = max(result, count)

print(result)