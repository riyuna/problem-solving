import sys
input=sys.stdin.readline
def quer_cmp(a):return (a[0]//sqrtn,a[1],a[2])
def last_cmp(a):return a[-1]

ans=[0]*(10**6+1)
n,m=map(int,input().split())
sqrtn=int(n**0.5)
L=list(map(int,input().split()))
qList=[]

for i in range(m):
    l,r=map(int,input().split())
    qList.append((l-1,r,i))
qres=[0]*len(qList)
qList.sort(key=quer_cmp)

d=0
check=[0]*(10**6+1)
first=qList[0]
s=first[0]
e=first[1]
for i in range(s,e):
    d-=check[L[i]]**2*L[i]
    check[L[i]]+=1
    d+=check[L[i]]**2*L[i]

qres[first[2]]=d

for i in range(1, len(qList)):

    while qList[i][0]<s:
        s-=1
        d-=check[L[s]]**2*L[s]
        check[L[s]]+=1
        d+=check[L[s]]**2*L[s]

    while qList[i][1]>e:
        d-=check[L[e]]**2*L[e]
        check[L[e]]+=1
        d+=check[L[e]]**2*L[e]
        e+=1
    
    while qList[i][0]>s:
        d-=check[L[s]]**2*L[s]
        check[L[s]]-=1
        d+=check[L[s]]**2*L[s]
        s+=1

    while qList[i][1]<e:
        e-=1
        d-=check[L[e]]**2*L[e]
        check[L[e]]-=1
        d+=check[L[e]]**2*L[e]

    qres[qList[i][2]]=d

for i in qres:print(i)