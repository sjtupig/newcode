s = input().strip()
num = 0
res = 1
for i in s:
    if i == '(':
        num += 1
    else:
        res *= num
        num -= 1
print(res)