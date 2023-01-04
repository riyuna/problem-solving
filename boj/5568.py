from itertools import permutations
n=int(input())
k=int(input())
L=[]
for i in ' '*n:L.append(input())
d=dict()
for i in permutations(L, k):
	s=''
	for j in i:s=s+j
	if s not in d:d[s]=True
ct=0
for i in d:ct+=1
print(ct)