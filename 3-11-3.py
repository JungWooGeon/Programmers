data = str(input())

state = data[0]
before = data[0]
result = 0

for i in range(1, len(data)):
    if data[i] == state:
        continue
    else:
        if before != state:
            continue
        before = data[i]
        result += 1

print(result)
