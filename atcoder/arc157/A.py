import sys
input = sys.stdin.readline
n,a,b,c,d=map(int,input().split())
if abs(b-c)>1:print('No')
elif b==c==0 and a*d!=0:print('No')
else:print('Yes')