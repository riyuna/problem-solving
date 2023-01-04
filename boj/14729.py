import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:
	L.append(float(input()))
L.sort()
def change(f):
	s=str(f)
	if f<10:
		return s+'0'*(5-len(s))
	if f==100:
		return '100.000'
	else:
		return s+'0'*(6-len(s))
for i in range(7):
	print(change(L[i]))