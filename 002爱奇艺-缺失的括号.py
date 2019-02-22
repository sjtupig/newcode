#把当前无法匹配的括号都放入栈中，可以匹配的出栈
s = input().strip()
stack = []
res = 0
for i in s:
	if not stack:
		stack.append(i)
	else:
		if i == '(':
			stack.append(i)
		else:
			if stack[-1] == '(':
				stack.remove(stack[-1])
			else:
				stack.append(i)
print(len(stack))

'''
分别记录左括号和右括号剩下的数量
S = input().strip()
#print(S)
n = len(S)
stack, res = 0, 0
for s in range(n):
    if S[s] == '(':
        stack += 1
    else:
        if stack > 0:
            stack -= 1
        else:
            res += 1
print(stack + res)

'''