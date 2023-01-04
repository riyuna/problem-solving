n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
newL=[]
a,b=map(int,input().split())
for i in L:
	newL.append(i+i[::-1])
newL+=newL[::-1]
for i in range(len(newL)):
	newL[i]=list(newL[i])
if newL[a-1][b-1]=='.':newL[a-1][b-1]='#'
else:newL[a-1][b-1]='.'
for i in newL:print(''.join(i))