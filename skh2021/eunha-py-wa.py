n,p,q,r=map(int,input().split())
s=input()
ans=0
L=list(s)

#skh count
for i in range(len(L)-2):
	if L[i]=='S' and L[i+1]=='K' and L[i+2]=='H':
		ans+=1
		L[i]=''
		L[i+1]=''
		L[i+2]=''

#one
for i in range(len(L)-1):
	if (L[i],L[i+1])==('K','H') and p:
		L[i]=''
		L[i+1]=''
		p-=1
		ans+=1
	if (L[i],L[i+1])==('S','H') and q:
		L[i]=''
		L[i+1]=''
		q-=1
		ans+=1
	if (L[i],L[i+1])==('S','K') and r:
		L[i]=''
		L[i+1]=''
		r-=1
		ans+=1

#two
ct_s=L.count('S')
ct_k=L.count('K')
ct_h=L.count('H')
x=min([ct_s,q,r])

ct=0
for i in range(x):
	y=min([p,ct_k,r-i])
	z=min([p,q-i,ct_h])
	if y+z<=p:
		ct=max(ct, i+y+z+min([p-y-z, q-i-y,r-i-z]))
	else: ct=max(ct,i+p)
ans+=ct

print(ans)