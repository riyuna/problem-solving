pL=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
L=[]
for i in range(len(pL)-1):
	L.append(pL[i]*pL[i+1])

n=int(input())
for i in L:
	if i>n:
		print(i)
		break