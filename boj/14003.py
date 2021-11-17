from bisect import bisect_left
n=int(input())
L=list(map(int,input().split()))
M=[]
mem=[]
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
print(len(mem))
for i in mem[::-1]:print(i,end=' ')