from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))



def bfs(x, y, index):
    q = deque()
    q.append((x, y))
    united = [(x, y)]
    count = 1
    summary = graph[x][y]
    union[x][y] = index

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    united.append((nx, ny))
                    q.append((nx, ny))
                    count += 1
                    summary += graph[nx][ny]
                    union[nx][ny] = index
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1

print(total_count)