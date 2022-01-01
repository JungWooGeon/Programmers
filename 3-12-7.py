n = str(input())

left_data = n[:len(n)//2]
right_data = n[len(n)//2:]

left = 0
for i in left_data:
    left += int(i)
right = 0
for i in right_data:
    right += int(i)

if left == right:
    print("LUCKY")
else:
    print("READY")