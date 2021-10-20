from math import gcd
s,n=input().split()
n=int(n)
if s=='order':
    if n==2: print(1,2)
    elif n==3:print(1, 3, 2)
    elif n==4:print(1, 3, 2, 4)
    elif n==5:print(1, 3, 5, 4, 2)
    else:
        print(3, end=' ')
        for i in range((n+1)//2):
            if i==1 or i==2:continue
            print(i*2+1, end=' ')
        print(5,end=' ')
        print(4,end=' ')
        for i in range(n//2):
            if i==1 or i==2:continue
            print(i*2+2,end=' ')
        print(6, end=' ')
else:
    pList=[True]*(2*10**6+1)
    pList[0]=False
    pList[1]=False
    P=[]
    for i in range(2, 2*10**6+1):
        if not pList[i]:continue
        for j in range(i*2, 2*10**6+1, i):
            pList[j]=False
        P.append(i)
    def solve(n):
        if n==2:return [1,2]
        if n==3:return [1,2,3]
        if n==4:return [1,2,3,4]
        if n==5:return [1,4,3,2,5]
        if n==6:return [1,4,3,2,5,6]
        odd=False
        if n%2:
            odd=True
            n+=1
        breaked=False
        for i in range(len(P)):
            for j in range(i):
                p,q=P[i],P[j]
                if pList[n+p] and pList[n+q] and gcd(p-q,n)==2:
                    breaked=True
                    break
            if breaked:break
        L=[1]
        for i in range(n-1):
            k=L[-1]
            if i%2==0:
                L.append((p-k)%n)
            else:
                L.append((q-k)%n)
        res=[]
        for i in L:
            if i!=0:res.append(i)
            else:
                if not odd:res.append(n)
        return res
    
    L=solve(n)
    for i in L:
        print(i,end=' ')