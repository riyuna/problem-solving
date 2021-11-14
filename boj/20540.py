s=input()
res=''
for i in s:
    if i=='E':res+='I'
    if i=='I':res+='E'
    if i=='S':res+='N'
    if i=='N':res+='S'
    if i=='T':res+='F'
    if i=='F':res+='T'
    if i=='J':res+='P'
    if i=='P':res+='J'
print(res)