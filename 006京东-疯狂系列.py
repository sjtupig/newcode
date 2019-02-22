import math
n = int(input().strip())
n_2 = int(math.sqrt(2*n))
if n <= n_2*(n_2+1)/2:
    print(n_2)
else:
    print(n_2+1)