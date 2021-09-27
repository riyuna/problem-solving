mob=[0]*1000001
mob[1]=1
for i in range(1, 1000001):
    for j in range(2*i, 1000001, i):
        mob[j]-=mob[i]


def f(n):
    c=0
    for i in range(1, int(n**0.5+1)):
        c+=mob[i]*(n//(i**2))
    return n-c
n=int(input())
l=n
r=10**12
while l!=r:
    mid=(l+r)//2
    s=f(mid)
    if s>=n:r=mid
    else:l=mid+1
print(l)