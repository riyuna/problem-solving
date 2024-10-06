import sys
input=sys.stdin.readline
n=int(input())
L=input().split()
d=dict()
d[1]=[]
d[2]=[]
d[3]=[]
d[4]=[]
d[5]=[]
for i in L:
	M=[0]
	for j in i:
		M.append(M[-1]+int(j))
	d[len(i)].append(M)
# print(d)
result = 0
#lengh 2
ct=[0]*10
for i in d[1]:
	ct[i[1]]+=1
for c in ct:result+=c**2

#length 4
ct2=[0]*20
ct3=[0]*30
ct4=[0]*40
ct5=[0]*50
for i in d[2]:
	ct2[i[-1]]+=1
for c in ct2:result+=c**2
#length 4: 1+3
for a,b,c,dd in d[3]:
	k=dd-b*2
	if 0<k<10:
		result += ct[k]
		# print((a,b,c,dd,k))
	k2=c*2-dd
	if 0<k2<10:
		result += ct[k2]
		# print((a,b,c,dd,k2))
	ct3[dd]+=1

#length 6: 3+3
for c in ct3:result+=c**2
#length 6: 2+4
for x1, x2, x3, x4, x5 in d[4]:
	k1=x5-2*x2
	k2=x4*2-x5
	if 0<k1<20:
		result+=ct2[k1]
		# print(x1,x2,x3,x4,x5,k1)
	if 0<k2<20:
		result+=ct2[k2]
		# print(x1,x2,x3,x4,x5,k2)
	ct4[x5]+=1
#length 6: 1+5
for x1, x2, x3, x4, x5, x6 in d[5]:
	ct5[x6]+=1
	k1=x6-x3*2
	k2=x4*2-x6
	if 0<k1<10:
		result+=ct[k1]
		# print(x1,x2,x3,x4,x5,x6,k1)
	if 0<k2<10:
		result+=ct[k2]
		# print(x1,x2,x3,x4,x5,x6,k2)

#length 8: 4+4
for c in ct4:result+=c**2

#length 8: 3+5
for x1, x2, x3, x4, x5, x6 in d[5]:
	k1=x6-x2*2
	k2=x5*2-x6
	if 0<k1<30:
		result+=ct3[k1]
		# print(x1,x2,x3,x4,x5,x6,k1)
	if 0<k2<30:
		result+=ct3[k2]
		# print(x1,x2,x3,x4,x5,x6,k2)

#length 10
for c in ct5:result+=c**2
print(result)