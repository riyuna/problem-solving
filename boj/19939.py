n,k=map(int,input().split())
if (k*(k+1))>2*n:print(-1)
else:
    if (k%2 and n%k==0) or (k%2==0 and n%(k//2)==0 and n//(k//2)%2):print(k-1)
    else:print(k)