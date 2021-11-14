n=int(input())
ct=0
while len(str(n))>1:
    s=str(n)
    res=1
    for i in s:res*=int(i)
    n=res
    ct+=1
print(ct)