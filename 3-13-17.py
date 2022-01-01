def bfs(graph, x, y):
    global temp

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < len(graph) and ny < len(graph):
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                temp.append([graph[nx][ny], nx, ny])
                for j in graph:
                    print(j)
                print()

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
x -= 1
y -= 1

data = [[]*(k+1) for _ in range(k+1)]
temp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data[graph[i][j]].append([i, j])

count = 0
while count != s:
    for d in data:
        if d == []:
            continue
        for index in d:
            bfs(graph, index[0], index[1])
    while temp:
        a, b, c = temp.pop(0)
        data[a].append([b, c])

    count += 1

print(graph[x][y])