L=list(map(int,input().split()))
M=[100,100,200,200,300,300,400,400,500]
score=sum(L)
hack=False
for i in range(9):
	if L[i]>M[i]:hack=True
if hack:print('hacker')
elif score<100:print('none')
else:print('draw')