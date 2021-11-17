def solve(L1, L2):
    L2.sort(reverse=True)
    d=dict()
    for i in L1:
        if i not in d:d[i]=0
        d[i]+=1
    for i in L2:
        if i in d and d[i]:
            d[i]-=1
        elif (i-1) in d and d[i-1]:
            d[i-1]-=1
        else:
            return False
    return True

for _ in ' '*int(input()):
    n=int(input())
    L1=list(map(int,input().split()))
    L2=list(map(int,input().split()))
    print(['NO', 'YES'][solve(L1, L2)])