s1=input()
s2=input()
L=[]
for i in range(8):
    L.append(int(s1[i]))
    L.append(int(s2[i]))
while len(L)>2:
    M=[]
    for i in range(len(L)-1):
        M.append(L[i]+L[i+1])
        M[-1]%=10
    L=M
print(M[0],end='')
print(M[1])