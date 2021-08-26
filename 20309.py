n=int(input())
L=list(map(int,input().split()))
state=True
for i in range(n):
    if (L[i]%2 and i%2) or (L[i]%2==0 and i%2==0):
        state=False
        break
if not state:print('NO')
else:print('YES')