s=input()
d=dict()
ct=0
for i in range(len(s)):
	for j in range(i+1, len(s)+1):
		ss=s[i:j]
		if ss not in d:
			d[ss]=True
			ct+=1
print(ct)