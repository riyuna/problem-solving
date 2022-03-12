for i in ' '*int(input()):
	s=input()
	L=[0]*8
	for j in range(38):
		sub=s[j:j+3]
		if sub=='TTT':L[0]+=1
		if sub=='TTH':L[1]+=1
		if sub=='THT':L[2]+=1
		if sub=='THH':L[3]+=1
		if sub=='HTT':L[4]+=1
		if sub=='HTH':L[5]+=1
		if sub=='HHT':L[6]+=1
		if sub=='HHH':L[7]+=1
	for i in L:print(i,end=' ')
	print()