a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
d=min([a/x, b/y, c/z])
print(a-x*d, b-y*d, c-z*d)