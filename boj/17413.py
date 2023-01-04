s=input()
res=''
store=''
bucket=False
for i in s:
	if bucket==True:
		res+=i
	if i=='<':
		bucket=True
		res+=store[::-1]
		store=''
		res+='<'
	if i=='>':
		bucket=False
		continue
	if not bucket and i!=' ':store+=i
	if not bucket and i==' ':
		res+=store[::-1]
		store=''
		res+=' '
res+=store[::-1]
print(res)