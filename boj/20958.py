n,m=map(int,input().split())
L=list(map(int,input().split()))
pL=[]
check=[True]*(4000)
check[0]=False
check[1]=False
for i in range(2, 4000):
    if not check[i]:continue
    pL.append(i)
    for j in range(i*2, 4000, i):
        check[j]=False

state=True
for i in range(n):
    if L[i]%7:
        state=False
        break
    L[i]//=7
    if L[i]%7==0:
        state=False
        break

ct=0

if state:
    for p in pL:
        if p**2>10**7:break
        checkL=[0]*100001
        rem=0
        for i in range(n):
            cnt=0
            while L[i]%p==0:
                L[i]//=p
                cnt+=1
            if rem<cnt:
                ct+=(cnt-rem)
                checkL[i+m-1]=(cnt-rem)
                rem=cnt
            rem-=checkL[i]
    
    d=dict()
    d[1]=1
    checkL=[0]*100001
    for i in range(n):
        if L[i] not in d:
            d[L[i]]=1
            checkL[i+m-1]=L[i]
            ct+=1
        if checkL[i]:
            del d[checkL[i]]
    
    print(ct)

else:print(-1)