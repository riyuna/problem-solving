n,m=map(int,input().split())
ct=0
while n:
    ct+=n
    n//=m
print(ct)