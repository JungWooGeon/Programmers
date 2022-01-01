n = int(input())

t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

print(t)
print(p)

data = [0]*(n)
for i in range(n, 0, -1):
    if t[i] <= (n-1) - i:
        data[i] = p[i]
        break

