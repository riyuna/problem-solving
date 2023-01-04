n=int(input())
a,b=map(int,input().split())
mod=10**9+7
print((pow(b-a,3,mod)*pow(6,mod-2,mod)*(n**2-1)*pow(n**2,mod-2,mod))%mod)