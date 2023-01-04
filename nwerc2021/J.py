n=int(input())
L = []
for i in ' '*n:L.append(tuple(map(int,input().split())))
L.append(L[0])
longitude = [False]*720
#longitude[i] : i/2-180 
#i deg -> i*2+360

pole = False
for i in range(n):
	start, end = L[i][1], L[i+1][1]
	# if abs(L[i][0]) == 90 or abs(L[i+1][1]) == 90:
	# 	pole=True
	# 	break
	if abs(start-end) == 180:
		pole = True
		break
	east = end-start
	west = start - end
	if east<0:east += 360
	if west<0:west += 360
	if east<west:
		pt = start
		while pt!=end:
			# print(pt)
			longitude[int(pt*2+360)] = True
			pt+=0.5
			if pt== 180: pt = -180
	
	else:
		pt = start
		while pt != end:
			longitude[int(pt*2+360)] = True
			pt-=0.5
			if pt==-180.5:pt=179.5

if sum(longitude)== 720 or pole:
	print('yes')
else:
	for i in range(720):
		if not longitude[i]:
			print(f'no {i/2-180:.1f}')
			break