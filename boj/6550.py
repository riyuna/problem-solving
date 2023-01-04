def sub(s1, s2):
	pt1=0
	pt2=0
	while pt1<len(s1):
		while pt2<len(s2) and s1[pt1]!=s2[pt2]:
			pt2+=1
		if pt2==len(s2):
			return False
		pt2+=1
		pt1+=1
	return True
while True:
	try:
		a,b=input().split()
		print(['No','Yes'][sub(a,b)])
	except:break