n=int(input())
s=input()
if n<4:print(0)
else:
    ct=0
    i=0
    while i<n-3:
        if s[i:i+4]=='pPAp':
            ct+=1
            i+=4
        else:i+=1
    print(ct)