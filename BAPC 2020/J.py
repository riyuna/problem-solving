c,e,m=map(int,input().split())
def is_square(n):
    if n<0:return False
    return int(n**0.5)**2==n

if c!=4:print('impossible')
elif is_square(e**2-16*m):
    k=int((e**2-16*m)**0.5)
    if (e+k)%4==0:
        print((e+k)//4+2, (e-k)//4+2)
    else:print('impossible')
else:print('impossible')