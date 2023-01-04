L=[]
n=int(input())
for i in ' '*n:
	s=input()
	L.append((float(s),s))
L.sort()
print(L[1][1])