L1=list(map(int,input().split()))
L2=list(map(int,input().split()))

if sum(L1)==sum(L2):print('Tie')
elif sum(L1)<sum(L2):print('Emma')
else:print('Gunnar')