a,b,g=map(int,input().split())
d1=dict()
d2=dict()
for i in input().split():
	d1[i]=True
for i in input().split():
	d2[i]=True
A=0
B=0
for i in input().split():
	if i in d1:A+=1
	if i in d2:B+=1

if A>B:print('A')
elif A<B:print('B')
else:print('TIE')