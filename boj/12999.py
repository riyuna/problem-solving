import sys
input=sys.stdin.readline
def quer_cmp(a):return (a[0]//sqrtn,a[1],a[2])
def last_cmp(a):return a[-1]

ans=[0]*(10**6+1)
n,m=list(map(int,input().split()))
sqrtn=int(n**0.5)
L=list(map(int,input().split()))
qList=[]

for i in range(m):
    l,r=map(int,input().split())
    qList.append((l-1,r,i))
qres=[0]*len(qList)
qList.sort(key=quer_cmp)

res=0
check=[0]*(10**6+1)
table=[0]*(10**6+1)
first=qList[0]
s=first[0]
e=first[1]

def plus(x,res):
    table[check[x]]-=1
    check[x]+=1
    table[check[x]]+=1
    res=max(res,check[x])
    return res

def minus(x,res):
    table[check[x]]-=1
    if check[x]==res and not table[check[x]]:
        res-=1
    check[x]-=1
    table[check[x]]+=1
    return res

for i in range(s,e):
    table[check[L[i]]]-=1
    check[L[i]]+=1
    table[check[L[i]]]+=1
    res=max(res,check[L[i]])

qres[first[2]]=res

for i in range(1, len(qList)):

    while qList[i][0]<s:
        s-=1
        res=plus(L[s],res)

    while qList[i][1]>e:
        res=plus(L[e],res)
        e+=1
    
    while qList[i][0]>s:
        res=minus(L[s],res)
        s+=1

    while qList[i][1]<e:
        e-=1
        res=minus(L[e],res)

    qres[qList[i][2]]=res

for i in qres:print(i)