s=input()
for i in s:
	k=0
	for j in str(ord(i)):
		k+=int(j)
	print(i*k)