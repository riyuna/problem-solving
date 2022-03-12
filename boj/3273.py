n=int(input())
L=sorted(list(map(int,input().split())))
k=int(input())
pt1=0
pt2=n-1
ct=0
while pt1<pt2:
	if L[pt1]+L[pt2]<k:
		pt1+=1
	elif L[pt1]+L[pt2]>k:
		pt2-=1
	else:
		ct+=1
		pt1+=1
		pt2-=1
print(ct)