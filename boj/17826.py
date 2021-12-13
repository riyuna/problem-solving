L=list(map(int,input().split()))
n=int(input())
L.sort(reverse=True)
rank=0
for i in range(50):
    if L[i]==n:rank=i+1
if rank<6:print('A+')
elif rank<16:print('A0')
elif rank<31:print('B+')
elif rank<36:print('B0')
elif rank<46:print('C+')
elif rank<49:print('C0')
else:print('F')