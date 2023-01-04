n=int(input())

left = 0
right = 0
for i in map(int,input().split()):
	if right<left:
		right+=i
	else:left+=i

d = abs(left-right)

ct=0
for i in [100, 50, 20, 10, 5, 2, 1]:
	ct+=d//i
	d%=i
print(ct)