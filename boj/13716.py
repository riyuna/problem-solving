from copy import deepcopy
n,k=map(int,input().split())
mod=10**9+7
class matrix:
    def __init__(self, L):
        self.list=L
    
    def __add__(self, other):
        res=[]
        for i in range(len(self.list)):
            L=[]
            for j in range(len(self.list[0])):
                L.append((self.list[i][j]+other.list[i][j])%mod)
            res.append(L)
        return matrix(res)
    
    def __str__(self):return str(self.list)
    
    def __mul__(self, other):
        res=[]
        for i in range(len(self.list)):
            L=[]
            for j in range(len(other.list[0])):
                c=0
                for k in range(len(self.list[0])):
                    c+=(self.list[i][k]*other.list[k][j])%mod
                    c%=mod
                L.append(c)
            res.append(L)
        return matrix(res)
    
    def __pow__(self, n):
        if n==1:return matrix(self.list)
        if n==2:return self*self
        perm=self**(n//2)
        res=(perm)*(deepcopy(perm))
        if n%2:res*=self
        return res

comb=[[0]*100 for i in range(100)]
comb[0][0]=1
for i in range(1, 100):
    for j in range(i+1):
        if i==j or j==0:comb[i][j]=1
        else:
            comb[i][j]=(comb[i-1][j]+comb[i-1][j-1])%mod
k+=1

L=[1]*(2*k)
L.append(0)
mtx1=matrix([L])
M=[]
C=[]
for i in range(k):
    perm=[]
    for j in range(k):
        perm.append(comb[j][i])
    C.append(perm)

for i in C:
    M.append([0]*k+i+[0])
for i in C:
    M.append(i+i+[0])
M[-1][-1]=1
M.append([0]*(2*k)+[1])
mtx2=matrix(M)

res=(mtx2**n)
res=mtx1*res
print(res.list[-1][-1])