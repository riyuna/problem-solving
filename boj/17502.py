n=int(input())
s=list(input())
for i in range(n//2):
    if s[i]=='?':
        if s[-i-1]=='?':
            s[i]='a'
            s[-i-1]='a'
        else:
            s[i]=s[-i-1]
    if s[-i-1]=='?':s[-i-1]=s[i]
if n%2 and s[n//2]=='?':s[n//2]='a'
ss=''.join(s)
print(ss)