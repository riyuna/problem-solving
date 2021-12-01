def solve(a,b):
    res=0
    res+=(a//3)*b
    a%=3
    res+=a*(b//3)
    b%=3
    if a*b==4:res+=2
    elif a*b==0:pass
    else:res+=1
    return res
for _ in ' '*int(input()):
    a,b=map(int,input().split())
    print(solve(a,b))