s=input()
h='HAPPY'
g='SAD'
hh=0
gg=0
for i in s:
	if i in h:hh+=1
	if i in g:gg+=1
if hh==gg==0:
	hh=1
	gg=1
print(f'{round((hh/(hh+gg)+0.000000001)*100, 2) :.2f}')