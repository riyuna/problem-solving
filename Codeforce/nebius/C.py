import sys
input=sys.stdin.readline
def solve(n, x, p):
    for i in range(1, min(n*2+2, p)+1):
        k=(i*(i+1))//2+x
        k%=n
        if k==0:return True
    return False

for i in ' '*int(input()):
    n,x,p=map(int,input().split())
    print(['No','Yes'][solve(n,x,p)])