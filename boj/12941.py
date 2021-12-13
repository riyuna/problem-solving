grun1=[0]
for i in range(1,1001):
    check=[]
    check.append(grun1[i-1])
    if i%2==0:check.append(grun1[i//2])
    pt=0
    while pt in check:pt+=1
    grun1.append(pt)

def g0(n):
    if n<3:return n
    return (n+1)%2

mem=dict()
def g1(n):
    if n<=1000:return grun1[n]
    if n in mem:return mem[n]
    if n%2:return 0
    k=g1(n//2)
    if k==1:
        mem[n]=2
        return 2
    mem[n]=1
    return 1

n,k=map(int,input().split())
res=0
L=list(map(int,input().split()))
if k%2==0:
    for i in L:res^=g0(i)
else:
    for i in L:res^=g1(i)

print('Kevin' if res else 'Nicky')