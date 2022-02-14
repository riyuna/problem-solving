h,w,n,m=map(int,input().split())
hh=h//(n+1)
ww=w//(m+1)
if h%(n+1):hh+=1
if w%(m+1):ww+=1
print(hh*ww)