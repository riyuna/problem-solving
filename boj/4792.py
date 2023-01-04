import sys
input=sys.stdin.readline
while True:
	n,m,k=map(int,input().split())
	if n==m==k==0:break
	L=[]
	for i in ' '*m:
		c,f,t=input().split()
		L.append([c,int(f), int(t)])
	L.sort()
	def prim(L, option='R'):
		visited=[0]*n
		ct=0
		s=0
		unionL=list(range(n))
		for c,a,b in L:
			k1=a-1
			k2=b-1
			e = 1 if c==option else 0
			while k1!=unionL[k1] or k2!=unionL[k2]:
				k1=unionL[k1]
				k2=unionL[k2]
			if k1!=k2:
				ct+=1
				s+=e
				visited[a-1]=1
				visited[b-1]=1
				k1=a-1
				k2=b-1
				while k1!=unionL[k1] or k2!=unionL[k2]:
					k1=unionL[k1]
					k2=unionL[k2]
				if k1<k2:unionL[k2]=unionL[k1]
				else:unionL[k1]=unionL[k2]
			if ct==n-1:return s
		return -1
	mx = n-1-prim(L)
	mn = prim(L[::-1],option='B')
	print(int(mn<=k<=mx))