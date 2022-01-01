def solution(N, stages):
    stages.sort()
    result = []
    for i in range(N+1):
        result.append((i, 0))

    count = 1
    population = len(stages)
    for i in range(len(stages)):
        if stages[i] >= N+1:
            break
        if i == len(stages)-1:
            result[stages[i]] = (stages[i], count / population)
            break
        if stages[i] == stages[i+1]:
            count += 1
        else:
            result[stages[i]] = (stages[i], count / population)
            population -= count
            count = 1

    result.pop(0)
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    
    answer = []
    for x in result:
        answer.append(x[0])
    return(answer)

print(solution(4, [4, 4, 4, 4, 4]))
