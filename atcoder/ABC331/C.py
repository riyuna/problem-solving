import sys
input=sys.stdin.readline
def linput():return list(map(int,input().split()))
n=int(input())
L=linput()
ctd=dict()
resd=dict()
for i in L:
	if i not in ctd:ctd[i]=0
	ctd[i]+=1
M=L[:]
M.sort(reverse=True)
resd[M[0]]=0
ct=0
for i in range(1, n):
	if M[i-1]>M[i]:
		ct+=M[i-1]*ctd[M[i-1]]
	resd[M[i]]=ct
for i in L:print(resd[i], end=' ')