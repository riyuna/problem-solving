d=dict()
def solve(x,y):
    if x==y==0:return 0
    if (x,y) in d: return d[(x,y)]
    res=0
    for i in range(1, 41):
        start=max(pow(2,i)-1, x)
        end=min(pow(2,i+1)-2, y)
        if start<=end:
            res=max(res, solve(start-pow(2, i)+1, end-pow(2, i)+1)+i)
    
    d[(x,y)]=res
    return res

for i in ' '*int(input()):
    x,y=map(int,input().split())
    print(solve(x,y))