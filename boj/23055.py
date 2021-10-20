n=int(input())
def solve(n):
    if n==1:return ['*']
    if n==2:return ['**', '**']
    L=[]
    L.append('*'*n)
    for i in range(n-2):
        blc=min(i,n-3-i)
        if n%2 and i==(n//2)-1:s='*'+' '*blc+'*'+' '*blc+'*'
        else:s='*'+' '*blc+'*'+' '*(n-blc*2-4)+'*'+' '*blc+'*'
        L.append(s)
    L.append('*'*n)
    return L
for i in solve(n):print(i)