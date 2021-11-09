x,y,z=map(int,input().split())
xx,yy,zz=map(int,input().split())
if y==yy:
    if x==xx:print('A')
    elif x<=xx*2:print('B')
    else:print('C')
elif y<=yy*2:print('D')
else:print('E')