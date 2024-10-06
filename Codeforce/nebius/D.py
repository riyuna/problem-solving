import sys
input=sys.stdin.readline

# def sol_max(L):
#     m=len(L)
#     check=[0]*m
#     res=0
#     two = m//4
#     for i in range(m-1):
#         if check[i]:continue
#         if two==0:break
#         if L[i]==L[i+1]==0:
#             check[i]=1
#             check[i+1]=1
#             two-=1

#     for i in range(m-1):
#         if check[i] or check[i+1]:continue
#         if two==0:break
#         if L[i]+L[i+1]<2:
#             check[i]=1
#             check[i+1]=1
#             two-=1
#             res+=1
#     ct=0
#     for i in range(m):
#         if not check[i] and L[i]==1:ct+=1
#     ct-=two
#     return ct+res

def sol_max(change,m):
    res=0
    two=m//4
    for i in range(len(change)):
        if two==0:break
        if change[i][0]==0:
            jj=change[i][1]//2
            change[i][1]-=min(jj, two)*2
            two-=min(jj, two)
    for i in range(len(change)):
        if two==0:break
        if change[i][0]==0 and change[i][1]!=0:
            if i!=0 and change[i-1][1]>0:
                change[i-1][1]-=1
                change[i][1]-=1
                two-=1
                res+=1
            elif i!=len(change)-1 and change[i+1][1]>0:
                change[i+1][1]-=1
                change[i][1]-=1
                two-=1
                res+=1
    ct=0
    for i in range(len(change)):
        if change[i][0]==1:ct+=change[i][1]
    ct-=two
    return ct+res

# def sol_min(L):
#     m=len(L)
#     check=[0]*m
#     res=0
#     two = m//4
#     for i in range(m-1):
#         if check[i]:continue
#         if two==0:break
#         if L[i]==L[i+1]==1:
#             check[i]=1
#             check[i+1]=1
#             two-=1
#             res+=1

#     for i in range(m-1):
#         if check[i] or check[i+1]:continue
#         if two==0:break
#         if L[i]+L[i+1]>0:
#             check[i]=1
#             check[i+1]=1
#             two-=1
#             res+=1
#     ct=0
#     for i in range(m):
#         if not check[i] and L[i]==1:ct+=1
#     return ct+res

def sol_min(change,m):
    res=0
    two=m//4
    for i in range(len(change)):
        if two==0:break
        if change[i][0]==1:
            jj=change[i][1]//2
            change[i][1]-=min(jj, two)*2
            res+=min(jj, two)
            two-=min(jj, two)
    for i in range(len(change)):
        if two==0:break
        if change[i][0]==0 and change[i][1]!=0:
            if i!=0 and change[i-1][1]>0:
                change[i-1][1]-=1
                change[i][1]-=1
                two-=1
                res+=1
            elif i!=len(change)-1 and change[i+1][1]>0:
                change[i+1][1]-=1
                change[i][1]-=1
                two-=1
                res+=1
    ct=0
    for i in range(len(change)):
        if change[i][0]==1:ct+=change[i][1]
    return ct+res
mx=0
mn=0
n,m=map(int,input().split())
for i in ' '*n:
    L=map(int,list(input().strip()))
    L=list(L)
    change = []
    for i in L:
        if len(change)==0 or change[-1][0]!=i:
            change.append([i, 1])
        else:change[-1][1]+=1
    change2=[]
    for i in change:change2.append(i[:])
    mx+=sol_max(change2,m)
    mn+=sol_min(change,m)
print(mn, mx)