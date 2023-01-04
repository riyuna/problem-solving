s1=input()
s2=input()
s=''
for i in s1:
	if i not in '0123456789':s=s+i
print(int(s2 in s))