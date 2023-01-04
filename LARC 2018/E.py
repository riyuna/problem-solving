import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:
	a,b=map(int,input().split())
	L.append((a,b))

vec_L=[]

for i in range(n):
	ii=(i+1)%n
	vector=(L[ii][0]-L[i][0], L[ii][1]-L[i][1])
	vec_L.append(vector)

tot=n*(n-1)*(n-2)//6

def check(vec1, vec2):
	x1,y1=vec1
	x2,y2=vec2
	return x1*y2-x2*y1

pt1=0
pt2=1
print(vec_L)
while pt1<n-1:
	while pt2<n and check(vec_L[pt1], vec_L[pt2])>0:
		pt2+=1
	if pt2==n:
		ct3=(pt2-pt1-2)*(pt2-pt1-1)//2
		print(pt1, pt2, 0, 0, ct3)
		tot-=ct3
		pt1+=1
		continue
	ct1=(n-1-pt2)*(n-pt2)//2
	ct2=(pt1)*(pt1+1)//2
	ct3=(pt2-pt1-2)*(pt2-pt1-1)//2 if check(vec_L[pt1],vec_L[pt2])!=0 else (pt2-pt1-1)*(pt2-pt1)//2
	tot-=ct1
	tot-=ct2
	tot-=ct3
	print(pt1, pt2, ct1, ct2, ct3)
	pt1+=1
print(tot)