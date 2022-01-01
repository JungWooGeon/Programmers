import heapq

n = int(input())
data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

result = 0
while len(data) > 1:
    x = heapq.heappop(data)
    y = heapq.heappop(data)
    result += x + y
    heapq.heappush(data, x+y)

print(result)