def f(n, k):
    a,b=n,k
    ct=2
    while True:
        a,b=b,a-b
        if b<0:return ct
        ct+=1

n=int(input())
res=0
rem=0
for i in range(1, n+1):
    k=f(n,i)
    if res<k:
        res=k
        rem=i
print(res)
print(n, rem, end=' ')
while True:
    n,rem=rem,n-rem
    if rem<0:break
    print(rem,end=' ')