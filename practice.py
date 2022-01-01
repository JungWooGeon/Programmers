t = int(input())

for i in range(t):
    n = int(input())
    
    dp0 = [0] * (n+1)
    dp1 = [0] * (n+1)

    for i in range(n+1):
        if i == 0:
            dp0[i] = 1
        elif i == 1:
            dp1[i] = 1
        else:
            dp0[i] = dp0[i-1] + dp0[i-2]
            dp1[i] = dp1[i-1] + dp1[i-2]

    print(dp0[n], dp1[n])