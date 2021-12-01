import sys
input=sys.stdin.readline

n,d=map(int,input().split())
p=[-1]*n
size=[1]*n
dic=dict()
dic[1]=n
mx=1
def find(a):
    if p[a]<0:return a
    k=max(size[a], size[p[a]])
    size[a],size[p[a]]=k,k
    p[a]=find(p[a])
    return p[a]

def merge(a,b):
    global mx
    a=find(a)
    b=find(b)
    if a==b:return-1
    dic[size[a]]-=1
    dic[size[b]]-=1
    newsz=size[a]+size[b]
    size[a], size[b]=newsz, newsz
    if newsz not in dic:dic[newsz]=0
    dic[newsz]+=1
    p[b]=a
    return 0

def mxk(k):
    L=[]
    for i in dic:
        for _ in range(dic[i]):L.append(i)
    L.sort(reverse=True)
    if len(L)<=k:return(sum(L))
    res=0
    for i in range(k):
        res+=L[i]
    return res

ct=1
for i in ' '*d:
    x,y=map(int,input().split())
    if x>y:x,y=y,x
    res=merge(x-1, y-1)
    if res==-1:ct+=1
    print(mxk(ct)-1)