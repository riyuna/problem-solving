m,s,g=map(int,input().split())
a,b=map(float,input().split())
l,r=map(int,input().split())
res1=int(l/a)+m//g
res2=int(r/b)+m//s
if res1<res2:print('friskus')
else:print('latmask')