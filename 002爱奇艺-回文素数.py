import math
L, R = map(int, input().strip().split(' '))
def isprime(n):
    if n <= 3: return n > 1
    if n%6!=1 and n%6!=5:return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i ==0 or n%(i+2)==0:
            return False 
    return True 
def isrever(s):
    return str(s) == str(s)[::-1]

res = 0
for i in range(L,R+1):
    if isprime(i) and isrever(i):
        res+=1
print(res)