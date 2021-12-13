n=int(input())
L=[]
for _ in ' '*n:L.append(int(input()))
lmem=0
rmem=0
lct=0
rct=0
for i in range(n):
    if L[i]>lmem:
        lmem=L[i]
        lct+=1
    if L[-i-1]>rmem:
        rmem=L[-i-1]
        rct+=1
print(lct)
print(rct)