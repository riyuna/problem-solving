import sys
input=sys.stdin.readline
def quer_cmp(a):return (a[0]//sqrtn,a[1],a[2])
def last_cmp(a):return a[-1]

ans=[0]*(10**6+1)
n=int(input())
sqrtn=int(n**0.5)
L=list(map(int,input().split()))
qList=[]

for i in range(int(input())):
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
    if check[L[i]]==0:d+=1
    check[L[i]]+=1

qres[first[2]]=d

for i in range(1, len(qList)):

    while qList[i][0]<s:
        s-=1
        if check[L[s]]==0:
            d+=1
        check[L[s]]+=1

    while qList[i][1]>e:
        if check[L[e]]==0:
            d+=1
        check[L[e]]+=1
        e+=1
    
    while qList[i][0]>s:
        if check[L[s]]==1:
            d-=1
        check[L[s]]-=1
        s+=1

    while qList[i][1]<e:
        e-=1
        if check[L[e]]==1:
            d-=1
        check[L[e]]-=1

    qres[qList[i][2]]=d

for i in qres:print(i)