def check(s):
	if s in "qwertasdfgzxcvb": return 1
	else:return 0

s=input()
state=True
for i in range(len(s)-1):
	if check(s[i])+check(s[i+1])!=1:
		state=False
print(['no','yes'][state])