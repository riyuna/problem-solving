n=int(input())
L=[]
for i in ' '*n:L.append(input())
ct=0
issa=False
iszimb=False
iszamb=False
for i in L:
	if i=='zambia':
		ct+=50 if not iszimb else 20
		iszamb=True
	elif i=='zimbabwe':
		if not iszamb:ct+=30
		iszimb=True
	else:
		iszamb=False
		iszimb=False
		if i=='namibia':
			if issa:ct+=40
			else:ct+=140
		elif i=='ethiopia':
			ct+=50
		elif i=='kenya':
			ct+=50
		elif i=='south-africa':
			issa=True
		elif i=='tanzania':
			ct+=50
		else:pass
print(ct)