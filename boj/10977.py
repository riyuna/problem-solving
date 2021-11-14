# pList=[]
# erat=[True]*1000001
# erat[0]=False
# erat[1]=False
# for i in range(2, 1001):
#     if not erat[i]:continue
#     pList.append(i)
#     for j in range(i*2, 10**6+1, i):
#         erat[i]=False

# def fact(n):
#     if n==1 or erat[n]:return [n]
#     for p in pList:
#         if n%p==0:
#             return fact[n//p]+[p]

def check(n, L):
    if len(L)%n!=0:return False
    for i in range(len(L)//n-1):
        for j in range(n):
            if L[j]!=L[i*n+n+j]:return False
    return True

for _ in ' '*int(input()):
    m,n=map(int,input().split())
    L=[]
    for _ in ' '*n:L.append(int(input()))
    L.append(L[0]+m)
    diff=[]
    for i in range(n):
        diff.append(L[i+1]-L[i])
    for i in range(1,n+1):
        if check(i, diff):
            print(m//(n//i))
            break