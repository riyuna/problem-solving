import sys
input = sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	s=input().strip()
	wina=0
	winb=0
	for x in range(1, n+1):
		cta=0
		ctb=0
		wa=0
		wb=0
		for i in range(n):
			if s[i]=='A':cta+=1
			else:ctb+=1
			if cta==x:wa+=1
			elif ctb==x:wb+=1
			if cta==x or ctb==x:
				cta=0
				ctb=0
		if (cta+ctb) or (wa==wb):continue
		else:
			if wa>wb:
				if s[-1]=='B':continue
				wina+=1
			else:
				if s[-1]=='A':continue
				winb+=1
			# print(x, wa, wb)
	if wina+winb==0:print('?')
	else:
		if wina==0:print('B')
		elif winb==0:print('A')
		else:print('?')