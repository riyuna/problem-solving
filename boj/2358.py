import sys
input=sys.stdin.readline
dictx=dict()
dicty=dict()
pt=dict()
for i in ' '*int(input()):
	a,b=map(int,input().split())
	if a not in dictx:dictx[a]=0
	if b not in dicty:dicty[b]=0
	if (a,b) not in pt:pt[(a,b)]=0
	pt[(a,b)]+=1
	dictx[a]+=1
	dicty[b]+=1

ct=0
for x in dictx:
	k=dictx[x]
	if k>1:ct+=1
for y in dicty:
	k=dicty[y]
	if k>1:ct+=1
# for p in pt:
# 	ct-=(pt[p]-1)
print(ct)