n,k=map(int,input().split())
L=sorted(list(map(int,input().split())))
mi=L[0]
v_min=L[0]*n
for i in range(1, len(L)):
    v_min=max(v_min, L[0]*i+L[i]*(n-i))
print((k-1)//v_min+1)