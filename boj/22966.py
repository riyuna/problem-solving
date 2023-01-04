L=[]
for i in ' '*int(input()):
	s,k=input().split()
	k=int(k)
	L.append((k,s))
L.sort()
print(L[0][1])