n=int(input())
L=[1,1]
while len(L)<=n:
    L.append((L[-1]+L[-2])%10)
print(L[n]%10)