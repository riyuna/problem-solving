r,b=map(int,input().split())
a=(r+4)+int(((r+4)**2-16*(b+r))**0.5)
a//=4
print(a, (r+4)//2-a)