n,m=map(int,input().split())
s=input().strip()
v='AEIOU'
L=[]

i2=-1
i3=-1
i4=-1

ct=0
for i in range(n-1, -1, -1):
    if s[i] not in v:
        i4=i
        break

for i in range(i4, -1, -1):
    if s[i]=='A':
        if ct==0:
            ct+=1
            i3=i
        else:
            i2=i
            break

if not(i2<i3<i4) or -1 in [i2, i3, i4]:print('NO')
else:
    for i in range(n):
        if i<i2:L.append(s[i])
    L.append(s[i2])
    L.append(s[i3])
    L.append(s[i4])
    if len(L)<m:print('NO')
    else:
        print('YES')
        for i in range(len(L)-m, len(L)):
            print(L[i],end='')