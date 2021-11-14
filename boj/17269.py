n,m=map(int,input().split())
s1,s2=input().split()
L=[]
pt1=0
pt2=0
while True:
    if pt1<n:L.append(s1[pt1])
    if pt2<m:L.append(s2[pt2])
    if pt1>=n and pt2>=m:break
    pt1+=1
    pt2+=1
rem=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
for i in range(len(L)):
    L[i]=rem[ord(L[i])-65]
while len(L)>2:
    M=[]
    for i in range(len(L)-1):
        M.append((L[i]+L[i+1])%10)
    L=M
print(f'{L[0]*10+L[1]}%')