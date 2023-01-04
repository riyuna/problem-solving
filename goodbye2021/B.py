for i in ' '*int(input()):
	n=int(input())
	state=True
	if n%3==0:
		if n%9:state=False
	if n%3==1:state=False
	print(['NIE','TAK'][state])