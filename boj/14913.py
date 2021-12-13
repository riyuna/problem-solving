a,d,k=map(int,input().split())
res=(k-a)//d+1
if (k-a)%d or res<1:print('X')
else:print(res)