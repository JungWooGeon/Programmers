import copy

def solution(key, lock):
    lock_data_len = (len(key)-1)*2+len(lock)
    lock_data = [[2]*(lock_data_len) for _ in range(lock_data_len)]

    for i in range(len(lock)):
        for j in range(len(lock)):
            lock_data[i+len(key)-1][j+len(key)-1] = lock[i][j]

    for _ in range(4):
        x = 0
        y = 0
        while True:
            isOk = True
            lock_copy = copy.deepcopy(lock_data)
            isbreak = False
            for i in range(len(key)):
                if isbreak:
                    break
                for j in range(len(key)):
                    if key[i][j] == 1 and lock_copy[x+i][y+j] == 1:
                        isbreak = True
                        break
                    if key[i][j] == 1 and lock_copy[x+i][y+j] == 0:
                        lock_copy[x+i][y+j] = 2
            
            for A in lock_copy:
                    if isOk == False:
                        break
                    for B in A:
                        if B == 0:
                            isOk = False
                            break
            if isOk:
                return True

            x += 1
            if len(key)-1 + len(lock) == x:
                x = 0
                y += 1
            if len(key)-1 + len(lock) == y:
                break

        N = len(key)
        ret = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = key[r][c]
        key = ret
    

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))