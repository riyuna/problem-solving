def find_p(n):
    L=[True]*(n+1)
    L[0]=False
    L[1]=False
    p_list=[]
    for i in range(2, n+1):
        if not L[i]:continue
        p_list.append(i)
        for j in range(i*2, n+1, i):L[j]=False
    return p_list

pL=find_p(40000)
l,r=map(int,input().split())
L=list(range(l,r+1))
res=[0]*(r-l+1)
for p in pL:
	rm=l%p
	if rm==0:rm=p
	for i in range(r//p-(l-1)//p):
		k=(p-rm)+i*p
		while L[k]%p==0:
			res[k]+=1
			L[k]//=p
for i in range(len(L)):
	if L[i]>1:
		res[i]+=1

d=dict()
L= [2,3,5,7,11,13,17,19,23,29,31]
for i in L:d[i]=True

ct=0
for i in res:
	if i in d:ct+=1
print(ct)