t = int(input())

answer = []

for re in range(t):
    n, m = map(int, input().split())

    temp = list(map(int, input().split()))

    data = []
    d = []

    index = 0
    for i in range(n):
        data.append([])
        d.append([])
        for j in range(m):
            data[index].append(temp.pop(0))
            if j == 0:
                d[index].append(data[index][j])
            else:
                d[index].append(0)
        index += 1

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = max(d[i][j-1], d[i+1][j-1]) + data[i][j]
            elif i == n-1:
                d[i][j] = max(d[i][j-1], d[i-1][j-1]) + data[i][j]
            else:
                max_value = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1])
                d[i][j] = max_value + data[i][j]

    result = []
    for i in d:
        result.append(max(i))

    answer.append(max(result))

for a in answer:
    print(a)