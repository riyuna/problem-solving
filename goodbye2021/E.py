d=dict()
n=int(input())
L=list(map(int,input().split()))
ignore=[False]*n
for i in range(n):
	if L[i] in d:
		ignore[i]=True
	d[L[i]]=True

d=dict()
d[0]=True
for i in range(n):
	if ignore[i]:continue
	k=L[i]
	mem=dict()
	for j in d:
		res=j^k
		if res in d:
			ignore[i]=True
			continue
		mem[res]=True
	for j in mem:d[j]=True
	if ignore[i]:continue

resL=[]
for i in range(1, n+1):
	if not ignore[i-1]:resL.append(i)

def solver(resL):
	ln=len(resL)
	if ln==1:return [resL[0]]
	res=solver(resL[:ln-1])
	L=res[:]
	L.append(resL[-1])
	for i in res:L.append(i)
	return L
	
M=solver(resL)
print(len(M))
for i in M:
	print(i)