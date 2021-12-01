n=int(input())
mod=10**9+7
L=[1,1]
for i in range(50):
    L.append((1+L[-1]+L[-2])%mod)
print(L[n])