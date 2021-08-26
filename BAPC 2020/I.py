n=int(input())
L=list(map(int,input().split()))

first=[False]*n
last=[False]*n

for i in range(n):
    if L[i]>3*n//4:
        last[i]=True

for i in range(n//4):
    last[n-i-1]=True

count2=0

for i in last:
    if i:count2+=1

for i in range(n):
    if count2==n//2:break
    if not last[i]:
        last[i]=True
        count2+=1

last_list=[]

for i in range(n):
    if last[i]:last_list.append(i+1)

res_L=[]
for i in last_list:res_L.append(L[i-1])
res_L.sort()

newL=L[:]
ct=0
for i in last_list:
    newL[i-1]=res_L[ct]
    ct+=1

L=newL[:]

for i in range(n):
    if L[i]<=n//4:
        first[i]=True

for i in range(n//4):
    first[i]=True

count1=0

for i in first:
    if i:count1+=1

for i in range(n):
    if count1==n//2:break
    if not first[i]:
        first[i]=True
        count1+=1

first_list=[]

for i in range(n):
    if first[i]:first_list.append(i+1)

mid_list = range(n//4+1, 3*n//4+1)

print(3)
for i in last_list:print(i,end=' ')
print()
for i in first_list:print(i,end=' ')
print()
for i in mid_list:print(i, end=' ')