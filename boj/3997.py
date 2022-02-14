n=int(input())
s=input()
d=dict()
ptsum=0
d[0]=1
def c(s):
    res=ord(s)
    if res<97:return res-65+26
    else: return res-97
for i in s:
    k=c(i)
    ptsum^=(1<<k)
    if ptsum not in d:d[ptsum]=0
    d[ptsum]+=1

ct=0
for i in d:
    k=d[i]
    ct+=k*(k-1)
    for bit in range(52):
        if i^(1<<bit) in d:
            ct+=k*d[i^(1<<bit)]
print(ct//2)