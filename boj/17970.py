n=int(input())
L=list(map(int,input().split()))
M=list(map(int,input().split()))

L1=[0]*n
M1=[0]*n
visited=[False]*n

for i in range(n):
    L[i]-=1
    M[i]-=1
    L1[L[i]]=i
    M1[M[i]]=i

success=False
result=[]

for i in range(n):
    if visited[i]:continue
    visited[i]=True
    state=True
    mem=[i]
    startL1, startL2=L1[i], L1[i]
    startM1, startM2=M1[i], M1[i]
    while len(mem)<n:
        last=mem[-1]
        l1=L[startL1-1]
        r1=L[(startL2+1)%n]
        l2=M[startM1-1]
        r2=M[(startM2+1)%n]
        if l1==l2:
            startL1-=1
            startL1%=n
            startM1-=1
            startM1%=n
            mem.append(l1)
            visited[l1]=True
        elif l1==r2:
            startL1-=1
            startL1%=n
            startM2+=1
            startM2%=n
            mem.append(l1)
            visited[l1]=True
        elif r1==l2:
            startL2+=1
            startL2%=n
            startM1-=1
            startM1%=n
            mem.append(r1)
            visited[r1]=True
        elif r1==r2:
            startL2+=1
            startL2%=n
            startM2+=1
            startM2%=n
            mem.append(r1)
            visited[r1]=True
        else:
            state=False
            break
    if state:
        success=True
        result=mem
        break

if success:
    for i in result:
        print(i+1,end=' ')
else:
    print(-1)