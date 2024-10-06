import sys
input=sys.stdin.readline

def check(L, ctL, mid, psum, m):
	n=len(L)
	aim = 0
	aimcost=0
	if mid < n+1: aim = ctL[-mid]
	ct = 0
	start = -1
	for i in range(n):
		if ctL[i]==aim:
			if start==-1:start=i
			ct+=1
			aimcost = L[i]
	# print('------')
	# print(L)
	# print(ctL)
	# print(mid, aim, aimcost)

	if ct<=aim-1:
		pay = ct*aimcost + psum[aim-1-ct]
		if pay<=m:return True
	if start > 0:
		k = psum[n-mid+1]-L[start-1]
		if k<=m:return True
	if psum[aim]<=m:return True
	return False


for i in ' '*int(input()):
	n,m=map(int,input().split())
	L=list(map(int,input().split()))
	L.sort()
	ctL=[0]*n
	psum=[0]
	for j in range(n):
		psum.append(psum[-1]+L[j])
		if j==0:ctL[j]=1
		else:
			ctL[j] = ctL[j-1] if L[j]==L[j-1] else j+1
	minp = n+1
	maxp = 1
	while minp>maxp:
		mid = (maxp+minp)//2
		if check(L, ctL, mid, psum, m):
			minp = mid
		else:
			maxp = mid+1
		#check midth place is possible
	print(maxp)
	# ctL2=ctL[:]
	# mm=m
	# wins = 0
	# wins2 = 0
	# elem2 = L[0]
	# iidx = 0
	# for j in range(n):
	# 	if elem2<L[j]:
	# 		elem2=L[j]
	# 		iidx = j
	# 		break
	# print(elem2, iidx)
	# for j in range(n):
	# 	if L[j]>m:break
	# 	else:
	# 		wins+=1
	# 		m-=L[j]
	# 		ctL[j]-=1
	# for j in range(iidx,n):
	# 	if L[j]>mm:break
	# 	else:
	# 		wins2 += 1
	# 		mm-=L[j]
	# 		ctL2[j]-=1
	# ct = 1
	# ct2 = 1
	# print(ctL)
	# print(ctL2)
	# print(wins, wins2)
	# for j in range(n):
	# 	if ctL[j]>wins:ct+=1
	# 	if ctL2[j]>wins2:ct2+=1
	# print(min(ct,ct2))