n=int(input())
L=list(range(1, n+1))
while len(L)>1:
    M=[]
    for i in range(1, len(L), 2):M.append(L[i])
    L=M
print(L[0])