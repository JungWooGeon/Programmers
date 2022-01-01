n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

data = [[0]*(n+1) for _ in range(n+1)]

data[1][1] = graph[0][0]
for i in range(1, n+1):
    for j in range(1, 501):
        if i < j or (i == 1 and j == 1):
            continue
        if j == 1:
            data[i][j] = data[i-1][j] + graph[i-1][j-1]
        elif j == i:
            data[i][j] = data[i-1][j-1] + graph[i-1][j-1]
        else:
            data[i][j] = max(data[i-1][j-1], data[i-1][j]) + graph[i-1][j-1]

print(max(data[n]))