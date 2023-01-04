from sys import stdout
while True:
	ln=0
	fin=False
	test = '0'
	for i in range(20):
		print(test*(i+1))
		stdout.flush()

		s=input()
		res = s.split()
		if res[1] == 'GRANTED':
			fin=True
			break
		if res[2] != '(5':
			ln=i+1
			break
	if fin:break

	result = ''
	pos='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for i in range(ln):
		for j in pos:
			imsi = result + j
			print(imsi+'0'*(ln-i-1))
			stdout.flush()

			s=input()
			res = s.split()
			if res[1] == 'GRANTED':
				fin=True
				break
			if int(res[2][1:]) > i*9+14:
				result = imsi
				break
		if fin:break
	
	if fin:break