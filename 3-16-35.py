n = int(input())
dp = [1]

x = 2
while True:
    temp = x
    while temp % 2 == 0:
        temp = temp // 2
    while temp % 3 == 0:
        temp = temp // 3
    while temp % 5 == 0:
        temp = temp // 5
    if temp == 1:
        dp.append(x)
    if len(dp) == n:
        break
    x += 1

print(dp)
print(dp[n-1])