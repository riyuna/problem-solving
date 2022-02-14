n=int(input())
L=[1,1]
for i in range(50):L.append(L[-1]+L[-2])
print(L[n-1], n-2)