a,b=map(int,input().split())
if a>b:a,b=b,a
if a%3 and a+1==b:print('Yes')
else:print('No')