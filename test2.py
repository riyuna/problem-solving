n=19645431593125
L=[]
for i in range(1, int(n**0.5)+1):
    j=int((n-i**2)**0.5)
    if i**2+j**2==n:
        print(i,j)
        L.append((i,j))
print(L)