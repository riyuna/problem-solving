import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dna=[]
for i in ' '*n:dna.append(input().strip())

def diff(s1, s2):
	ct=0
	for i in range(len(s1)):
		if s1[i]!=s2[i]:ct+=1
	return ct

L=[]

for i in range(n):
	for j in range(i):
		L.append([diff(dna[i],dna[j]), i+1, j+1])

L.sort()
visited=[0]*n
ct=0
s=0
tree=[]
unionL=list(range(n))
for e,a,b in L:
	k1=a-1
	k2=b-1
	while k1!=unionL[k1] or k2!=unionL[k2]:
		k1=unionL[k1]
		k2=unionL[k2]
	if k1!=k2:
		ct+=1
		s+=e
		tree.append((b-1,a-1))
		visited[a-1]=1
		visited[b-1]=1
		k1=a-1
		k2=b-1
		while k1!=unionL[k1] or k2!=unionL[k2]:
			k1=unionL[k1]
			k2=unionL[k2]
		if k1<k2:unionL[k2]=unionL[k1]
		else:unionL[k1]=unionL[k2]
	if ct==n-1:break


print(s)
tree.sort()
for i, j in tree:print(i,j)