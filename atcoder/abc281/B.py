import sys
input = sys.stdin.readline
s=input().rstrip()
res=True
if len(s)==8:
	for i in range(8):
		if i == 0 or i==7:
			if s[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				res=False
				break
		else:
			if s[i] not in '1234567890':
				res=False
				break
		if i==1 and s[i] =='0':
			res=False
			break
else:res=False
print(['No','Yes'][res])