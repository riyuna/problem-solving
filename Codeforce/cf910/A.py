import sys
input=sys.stdin.readline

for i in ' '*int(input()):
	n,k=map(int,input().split())
	s=input().strip()
	ct=s.count("B")
	if ct==k:
		print(0)
		continue
	elif ct>k:
		pt=0
		while ct>k:
			if s[pt]=='B':ct-=1
			pt+=1
		print(1)
		print(pt, 'A')
	else:
		pt=0
		while ct<k:
			if s[pt]=='A':ct+=1
			pt+=1
		print(1)
		print(pt, 'B')