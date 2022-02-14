a,b,c,d=map(int,input().split())
s=(c-a)*60+(d-b)
if s<0:s+=1440
print(s, s//30)