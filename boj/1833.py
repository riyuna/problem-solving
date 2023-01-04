import sys
input=sys.stdin.readline
n=int(input())
data=[]
for i in ' '*n:data.append(list(map(int,input().split())))
L=[]
res = 0
for i in range(n):
	for j in range(i):
		if data[i][j]<0:res+=abs(data[i][j])
		L.append([max(0, data[i][j]), j+1, i+1])
L.sort()
visited=[0]*n
ct=0
cost=0
rem=[]
unionL=list(range(n))
for e,a,b in L:
    k1=a-1
    k2=b-1
    while k1!=unionL[k1] or k2!=unionL[k2]:
        k1=unionL[k1]
        k2=unionL[k2]
    if k1!=k2:
        ct+=1
        cost+=e
        if e:rem.append([a,b])
        visited[a-1]=1
        visited[b-1]=1
        k1=a-1
        k2=b-1
        while k1!=unionL[k1] or k2!=unionL[k2]:
            k1=unionL[k1]
            k2=unionL[k2]
        if k1<k2:unionL[k2]=unionL[k1]
        else:unionL[k1]=unionL[k2]
    if ct==n-1:break
print(cost+res, len(rem))
for a,b in rem:print(a,b)