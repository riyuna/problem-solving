L=[
    '000000'
    ,'001111'
    ,'010011'
    ,'011100'
    ,'100110'
    ,'101001'
    ,'110101'
    ,'111010'
]
d=dict()
for i in range(len(L)):
    d[L[i]]=chr(i+65)
def solve(s):
    if s in d:return d[s]
    res=''
    for i in d:
        diff=0
        for j in range(len(s)):
            if i[j]!=s[j]:diff+=1
        if diff==1:res=i
    if len(res):return d[res]
    return False

n=int(input())
s=input()
L=[]
bk=-1
for i in range(n):
    ss=s[i*6:(i+1)*6]
    k=solve(ss)
    if not k:
        bk=i+1
        break
    else:L.append(k)
if bk>0:print(bk)
else: print(''.join(L))