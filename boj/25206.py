grade=0
ct=0
for i in range(20):
	a,b,c=input().split()
	if c=='P':continue
	else:
		k=69-ord(c[0])
		if c=='F':
			k=0
		else:
			if c[-1]=='+':k+=0.5
	ct+=float(b)
	grade+=k*float(b)
print(grade/ct)