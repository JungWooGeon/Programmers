from itertools import combinations
import copy

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

all_cases = []
teachers = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            all_cases.append([i, j])
        if graph[i][j] == 'T':
            teachers.append([i, j])

three_cases = list(combinations(all_cases, 3))

def watch(graph, x, y):
    temp_x = x
    temp_y = y
    while temp_y >= 0:
        if graph[temp_x][temp_y] == 'S':
            return False
        if graph[temp_x][temp_y] == 'O':
            break
        temp_y -= 1
    temp_y = y
    while temp_y < n:
        if graph[temp_x][temp_y] == 'S':
            return False
        if graph[temp_x][temp_y] == 'O':
            break
        temp_y += 1
    temp_y = y
    while temp_x >= 0:
        if graph[temp_x][temp_y] == 'S':
            return False
        if graph[temp_x][temp_y] == 'O':
            break
        temp_x -= 1
    temp_x = x
    while temp_x < n:
        if graph[temp_x][temp_y] == 'S':
            return False
        if graph[temp_x][temp_y] == 'O':
            break
        temp_x += 1
    return True 


result = []
for cases in three_cases:
    graph_copy = copy.deepcopy(graph)
    for case in cases:
        graph_copy[case[0]][case[1]] = 'O'
    
    isTrue = True
    for teacher in teachers:
        if not watch(graph_copy, teacher[0], teacher[1]):
            isTrue = False
            break

    result.append(isTrue)

if True in result:
    print('YES')
else:
    print('NO')