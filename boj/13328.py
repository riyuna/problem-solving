import sys
sys.setrecursionlimit(10000)
import copy
mod=31991
def f(L,M):
    L1=[[0]*len(L)for i in range(len(L))]
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                L1[i][j]+=(L[i][k]*M[k][j])
                L1[i][j]%=mod
    return L1
def mul(L,n):
    if n==0:return L
    if n==1:
        for i in L:
            for j in range(len(i)):
                i[j]%=mod
        L1=copy.deepcopy(L)
        return L1
    M1=mul(L,n//2)
    M=f(M1,M1)
    if n%2:return f(M,L)
    else:return M

d,t=map(int,input().split())

mtrix=[[1]*d]
for i in range(d-1):
	L=[0]*d
	L[i]=1
	mtrix.append(L)

L=[pow(2,i-1,mod) if i else 1 for i in range(d)]
res=0

if t<d:
	print(L[t])
else:
	M=mul(mtrix,t-d+1)
	for i in range(d):
		res+=M[0][i]*L[-i-1]
		res%=mod
	print(res)