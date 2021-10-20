n,k=map(int,input().split())
def fact(n):
    if n==0:return 1
    else:return fact(n-1)*n
print(fact(n-1)/fact(n-k)/fact(k-1))