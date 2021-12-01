a,b,c=sorted(list(map(int,input().split())))
state=False
if a+b==c:state=True
if a==b or b==c: state=True
print(['N', 'S'][state])