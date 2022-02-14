a,b=map(int,input().split())
d=a**2-b
sqt=int(d**0.5)
if sqt==0:
    print(-a)
else:
    print(-a-sqt, -a+sqt)