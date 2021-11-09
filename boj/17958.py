s=input()
def solve(s):
    n=len(s)
    L=list(s)
    L.sort()
    freq=[0]*26
    ct=0
    for i in range(26):
        ii=chr(i+97)
        freq[i]=L.count(ii)
        if freq[i]:ct+=1
    mx=max(freq)
    if n==2:
        if s[0]==s[1]:
            return False
        else: return L
    if n==4:
        if mx>2:return False
        else:return L
    if mx>n-2:return False
    if mx==n-2 and ct==2:return False
    mx_str=''
    for i in range(26):
        if freq[i]==mx:mx_str=chr(i+97)
    M=[mx_str]*mx
    res=[]
    for i in L:
        if i!=mx_str:res.append(i)
    if mx>n//2:
        return M[:n//2]+[res[0]]+M[n//2:]+res[1:]
    else:return L

L=solve(s)
if L==False:print('NO')
else:
    print('YES')
    print(''.join(L))