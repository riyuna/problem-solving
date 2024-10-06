import sys
input = sys.stdin.readline
n,k,m,f=map(int,input().split())
L=[0]*n
for i in range(k):
	for j in list(map(int,input().split())):
		L[j-1]|=1<<i
d=dict()
for i in range(n):
	if L[i] not in d:d[L[i]]=[]
	d[L[i]].append(i+1)
for _ in ' '*f:
	s=input().strip()
	now=0
	ct=0
	for i in range(len(s)):
		if s[i]=='Y':now^=(1<<ct)
		ct+=1
	if now not in d or len(d[now])>1:
		print(0)
	else:print(d[now][0])