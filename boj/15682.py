from decimal import *
getcontext().prec = 100
f=lambda a,b,c,d,x:a*x*x*x+b*x*x+c*x+d
def bin_search(l, h, a,b,c,d):
	if f(a,b,c,d,l)*f(a,b,c,d,h)>0:return None
	m=(l+h)/Decimal(2)
	while (h-l)>Decimal(10)**Decimal(-20):
		ll = f(a,b,c,d,l)
		hh = f(a,b,c,d,h)
		m = (l+h)/Decimal(2)
		mm = f(a,b,c,d,m)
		if ll*mm>0:l=m
		else:h=m
	return m

def solve(a,b,c,d):
	dd=b**Decimal(2)-Decimal(3)*a*c
	det = b**2*c**2 - 4*a*c**3 - 4*b**3*d - 27*a**2*d**2 + 18*a*b*c*d
	if det<0:
		return [bin_search(Decimal(-1000000), Decimal(1000000), a,b,c,d)]
	else:
		x1 = (-b+Decimal((dd)**Decimal('0.5')))/(Decimal(3)*a)
		x2 = (-b-Decimal((dd)**Decimal('0.5')))/(Decimal(3)*a)
		if x1>x2:x1,x2=x2,x1
		if round(f(a,b,c,d,x1), 20) == 0:return [x1] if abs(x1-x2) < Decimal(10)**Decimal(-11) else [x1, bin_search(x2, 1000000, a,b,c,d)]
		if round(f(a,b,c,d,x2), 20) == 0:return [bin_search(-1000000, x1, a, b, c, d), x2]
		L=[bin_search(-1000000,x1,a,b,c,d), bin_search(x1,x2,a,b,c,d), bin_search(x2,1000000,a,b,c,d)]
		M=[]
		for i in L:
			if i!= None: M.append(i)
		M.sort()
		res = []
		for i in M:
			if len(res)==0:res.append(i)
			else:
				if abs(i-res[-1])>Decimal(10)**Decimal(-11):res.append(i)
		return res

for i in ' '*int(input()):
	a,b,c,d=map(Decimal, input().split())
	L=solve(a,b,c,d)
	for i in L:
		s='%.10f'%i
		if s=='-0.0000000000':s=0
		print(s,end=' ')
	print()