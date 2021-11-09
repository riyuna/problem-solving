n,p=map(int,input().split())
ct=1
for i in range(1,n+1):
    ct*=i
    ct%=p
print(ct)