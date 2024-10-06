n=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)

pList=[]
check=[True]*(10001)
check[0]=False
check[1]=False
for i in range(2, 10001):
    if not check[i]:continue
    pList.append(i)
    for j in range(i*2, 10001, i):
        check[j]=False
factmem=dict()
def fact(n):
    if n in factmem:return factmem[n]
    result = dict()
    for i in pList:
        if n%i==0:
            ct=0
            while n%i==0:
                ct+=1
                n//=i
            result[i]=ct
    if n!=1:result[n]=1
    factmem[n]=result
    return result

divmem=dict()
divmem[1]=[1]

def div(n, ft=None):
    if n in divmem:return divmem[n]
    if ft==None:ft=fact(n)
    d=list(ft.keys())[0]
    newn=n//(d**ft[d])
    newft=ft.copy()
    del(newft[d])
    newndiv=div(newn, newft)
    divres=[]
    for i in newndiv:
        for j in range(ft[d]+1):
            divres.append(i*pow(d, j))
    divres.sort()
    divmem[n]=divres
    return divres

mem=dict()
res=[]
for i in L:
    if i not in mem:res.append(i)
    for d in div(i):
        mem[d]=False
res.sort()
for i in res:print(i,end=' ')