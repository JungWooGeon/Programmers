data = str(input())

result = 0
for d in data:
    if result == 0 or d == 0 or d == 1 or result == 1:
        result += int(d)
    else:
        result *= int(d)

print(result)
