a,b,c=map(int,input().split())
res=[(a+b+c)//3]*3
for i in range((a+b+c)%3):res[2-i]+=1
aa=a-res[0]
bb=b-res[1]
cc=c-res[2]
res=0
res+=min(abs(aa), abs(cc))*2
print(res+abs(bb))