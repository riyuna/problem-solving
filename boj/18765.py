def make(n):
	s=str(n)
	if len(s)==1:
		if s=='0':return '+[]'
		if s=='1':return '+!![]'
		if s=='2':return '!![]+!![]'
		if s=='3':return '!![]+!![]+!![]'
		if s=='4':return '!![]+!![]+!![]+!![]'
		if s=='5':return '!![]+!![]+!![]+!![]+!![]'
		if s=='6':return '!![]+!![]+!![]+!![]+!![]+!![]'
		if s=='7':return '+!![]+[+[]]-!![]-!![]-!![]'
		if s=='8':return '+!![]+[+[]]-!![]-!![]'
		if s=='9':return '+!![]+[+[]]-!![]'
	else:
		ss=''
		for i in s:
			k=make(i)
			ss+=('['+k+']')
			ss+='+'
		return ss[:len(ss)-1]+'-[]'
for i in range(1001):
	s=make(i)
	print(s)