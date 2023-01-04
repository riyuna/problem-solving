a,b=input().split()
def check(s1, s2):
	if s1==s2:return False
	if s1[0]==s2[0]:return True
	if ord('f')-min(ord('f'),ord(s1[0]))+int(s1[1:])==ord('f')-min(ord('f'),ord(s2[0]))+int(s2[1:]):return True
	if max(ord('f'),ord(s1[0]))-ord('f')+int(s1[1:])==max(ord('f'),ord(s2[0]))-ord('f')+int(s2[1:]):return True
	return False
ct=0
for i in range(1, 12):
	if i<7:
		for j in 'abcdefghijk':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1
	if i==7:
		for j in 'bcdefghij':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1
	if i==8:
		for j in 'cdefghi':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1
	if i==9:
		for j in 'defgh':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1
	if i==10:
		for j in 'efg':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1
	if i==11:
		for j in 'f':
			s=j+str(i)
			if check(s,a) and check(s,b):
				# print(s)
				ct+=1

print(ct)