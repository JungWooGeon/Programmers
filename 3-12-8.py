n = str(input())

al = ''
num = 0

for x in n:
    if x.isdigit():
        num += int(x)
    else:
        al += x

al = sorted(al)
alpha = ''
for x in al:
    alpha += x

print(alpha+str(num))