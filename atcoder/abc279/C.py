import sys
input=sys.stdin.readline
h,w=map(int,input().split())
s=[[]for i in range(w)]
for i in ' '*h:
	ip = input()
	for j in range(w):
		s[j].append(ip[j])
t=[[]for i in range(w)]
for i in ' '*h:
	ip = input()
	for j in range(w):
		t[j].append(ip[j])
	
s.sort()
t.sort()
if s==t:print('Yes')
else:print('No')