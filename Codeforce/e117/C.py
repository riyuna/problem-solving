import sys
input=sys.stdin.readline
def solve(k,x):
    if x>=k**2:return (2*k-1)
    if x<=(k*(k-1))//2:
        xx=int((2*x)**0.5)-1
        while not ((xx*(xx+1))//2 < x <= (xx+1)*(xx+2)//2):
            xx+=1
        return xx+1
    res=k-1
    x-=k*(k-1)//2
    x=k*(k+1)//2-x
    xx=int((2*x)**0.5)-1
    while not (xx*(xx+1)//2 <= x < (xx+1)*(xx+2)//2):
        xx+=1
    return (k-xx)+res

for _ in ' '*int(input()):
    k,x=map(int,input().split())
    print(solve(k,x))