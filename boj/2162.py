n=int(input())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))
p=[-1]*(n)

def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1=ccw(x1,y1,x2,y2,x3,y3)
    ccw2=ccw(x1,y1,x2,y2,x4,y4)
    ccw3=ccw(x3,y3,x4,y4,x1,y1)
    ccw4=ccw(x3,y3,x4,y4,x2,y2)
    if ccw1*ccw2==ccw3*ccw4==0:
        if x1==x2==x3==x4:
            return not(min(y3,y4)>max(y1,y2) or min(y1,y2)>max(y3,y4))
        return not(min(x3,x4)>max(x1,x2) or min(x1,x2)>max(x3,x4))
    return ccw1*ccw2<=0 and ccw3*ccw4<=0

for i in range(n):
    for j in range(i+1, n):
        x1,y1,x2,y2=L[i]
        x3,y3,x4,y4=L[j]
        if cross(x1,y1,x2,y2,x3,y3,x4,y4):
            merge(i,j)

d=dict()
ct=0
mx=0
for i in range(n):
    if p[i]==-1:
        d[i]=0
        ct+=1
for i in range(n):
    d[find(i)]+=1
for i in d:
    if d[i]>mx:mx=d[i]
print(ct)
print(mx)