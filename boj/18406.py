n=input()
l=len(n)
a,b=0,0
for i in range(l//2):
	a+=int(n[i])
	b+=int(n[i+l//2])
print(['READY', 'LUCKY'][a==b])