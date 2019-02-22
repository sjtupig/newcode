#这题的关键是找到字符串的字回文串，原串长度加上两者之差
s = input().strip()
sr = s[::-1]
f = False
if s == s[::-1]:
    print(len(s))
else:
	for i in range(len(s)):
		if s[i:] == sr[:len(s)-i]:
			print(len(s)+i)
			f = True
			
			break
	if not f:
		print(len(s)+len(s)-1)