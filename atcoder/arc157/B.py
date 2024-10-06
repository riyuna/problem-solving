import sys
input = sys.stdin.readline
n,k=map(int,input().split())
s=input().strip()
now=0
for i in range(n-1):
    if s[i]==s[i+1]=='Y':now+=1
L=[]
M=[]
ct=0
ct2=0
if s[0]=='Y':L.append(0)
for i in s:
    if i=='X':ct+=1
    else:
        if ct:L.append(ct)
        ct=0
if s[0]=='X':M.append(0)
for i in s:
    if i=='X':
        if ct2:M.append(ct2)
        ct2=0 
    else:
        ct2+=1
L.append(ct)
M.append(ct2)
# print(L)
# print(M)
check=False
if len(L)==1:
    st=L[0]
    ed=0
    L=[]
    check=True
else:
    st=L.pop(0)
    ed=L.pop(-1)
L.sort()
# print(st, ed, L)
for i in L:
    if k==0:break
    if i<=k:
        k-=i
        now+=(i+1)
    else:
        now+=k
        k=0
    if k==0:break
if k:
    if st+ed>=k:
        now+=(k-check)
        k=0
    else:
        now+=(st+ed)
        k-=(st+ed)
if len(M)==1:
    st=M[0]
    ed=0
    M=[]
else:
    st=M.pop(0)
    ed=M.pop(-1)

if k:
    if st>=k:
        now-=k
        k=0
    else:
        now-=st
        k-=st
    if k==0:pass
    elif ed>=k:
        now-=k
        k=0
    else:
        now-=ed
        k-=ed

M.sort(reverse=True)
for i in M:
    if k==0:break
    if i>=k:
        now-=(k+1)
        k=0
    else:
        now-=(i+1)
        k-=i
    if k==0:break
print(max(now, 0))