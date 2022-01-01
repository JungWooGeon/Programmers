
def solution(s):
    if len(s) == 1:
        return 1
    data = ['']*(len(s)//2 + 1)

    for i in range(1, len(s)//2 + 1):
        previous = s[:i]
        now = ''
        data_count = 1
        count = 0
        for j in range(i, len(s)):
            now += s[j]
            count += 1
            if count == i:
                if previous == now:
                    data_count += 1
                    now = ''
                    if j == len(s)-1:
                        data[i] += str(data_count) + previous
                else:
                    if data_count > 1:
                        data[i] += str(data_count) + previous
                    else:
                        data[i] += previous
                    data_count = 1
                    previous = now
                    if j == len(s)-1:
                        data[i] += now
                    now = ''
                count = 0
            else:
                if j == len(s)-1:
                    if data_count > 1:
                        data[i] += str(data_count) + previous + now
                    else:
                        data[i] += previous + now

    min = len(data[1])
    for i in range(1, len(data)):
        if data[i] == '':
            continue
        if len(data[i]) < min:
            min = len(data[i])

    return min

print(solution('a'))



# def solution(s):
#     answer = len(s)
#     for step in range(1, len(s)//2 + 1):
#         compressed = ""
#         prev = s[0:step]
#         count = 1
#         for j in range(step, len(s), step):
#             if prev == s[j:j+step]:
#                 count += 1
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j+step]
#                 count = 1
#         compressed += str(count) + prev if count >= 2 else prev
#         answer = min(answer, len(compressed))
#     return answer