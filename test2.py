s=input()
n=len(s)
k=n//4
if n%4!=0:k+=1
for i in range(k):
    spl = s[i*4:min(i*4+4, n)]
    if len(spl)<4:spl=spl+'0'*(4-len(spl))
    j=hex(int(spl,2))
    print(j[2:],end='')