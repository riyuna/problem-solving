a,b,c=sorted(list(map(int,input().split())))
k=int(input())
if a*100+b*10+c==k:print(1)
if a*100+c*10+b==k:print(2)
if b*100+a*10+c==k:print(3)
if b*100+c*10+a==k:print(4)
if c*100+a*10+b==k:print(5)
if c*100+b*10+a==k:print(6)