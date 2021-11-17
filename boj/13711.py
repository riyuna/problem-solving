from bisect import bisect_left

n=int(input())
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))

def lis(L):
    M=[]
    mem=[]
    n=len(L)
    pair=[[0,0]for i in range(n)]
    M.append(L[0])
    pair[0][0]=L[0]
    pair[0][1]=0
    pt=0
    for i in range(1, n):
        if M[pt]<L[i]:
            M.append(L[i])
            pt+=1
            pair[i][0]=L[i]
            pair[i][1]=pt
        else:
            k=bisect_left(M, L[i])
            M[k]=L[i]
            pair[i][0]=L[i]
            pair[i][1]=k

    for i in range(n-1, -1, -1):
        if pair[i][1]==pt:
            mem.append(pair[i][0])
            pt-=1
    return(len(mem))

M1=[0]*n
M2=[0]*n
for i in range(n):
    M2[L2[i]-1]=i

for i in range(n):
    M1[i]=M2[L1[i]-1]
print(lis(M1))