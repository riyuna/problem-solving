import itertools
base=[0,0,0]
def hit(base):
    run=base[2]
    L=[1,base[0],base[1]]
    return (L,run)
def hit2(base):
    run=base[1]+base[2]
    L=[0,1,base[0]]
    return (L,run)
def hit3(base):
    run=sum(base)
    return ([0,0,1],run)
def hit4(base):
    return ([0,0,0],sum(base)+1)

L=[]
n=int(input())
for i in ' '*n:L.append(list(map(int,input().split())))
hitter=[2,3,4,5,6,7,8,9]
mx=0
for i in itertools.permutations(hitter):
    i=list(i)
    base=[0,0,0]
    pos=0
    totrun=0
    inning=1
    out=0
    while inning<=n:
        res=L[inning-1]
        if pos==3:ht=1
        else:ht=i[pos] if pos<3 else i[pos-1]
        r=res[ht-1]
        if r==0:
            out+=1
        else:
            if r==1:
                tup=hit(base)
            if r==2:
                tup=hit2(base)
            if r==3:
                tup=hit3(base)
            if r==4:
                tup=hit4(base)
            base=tup[0]
            totrun+=tup[1]
        pos+=1
        if pos==9:pos=0
        if out==3:
            base=[0,0,0]
            out=0
            inning+=1
    if totrun>mx:mx=totrun
print(mx)