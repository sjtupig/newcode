l = input().strip().split(' ')
s1 = l[0]
n1 = int(l[1])
s2 = l[2]
n2 = int(l[3])
str1 = ''.join([s1 for i in range(n1)])
str2 = ''.join([s2 for i in range(n2)])
if int(str1) < int(str2):
    print('Less')
elif int(str1) == int(str2):
    print('Equal')
else:
    print('Greater')