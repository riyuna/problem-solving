n=int(input())
s=input()
#j=apple, p=orange

def check(s):
    stack=[]
    mx=0
    apple=0
    orange=0
    for i in s:
        if i=='j':apple+=1
        else:orange+=1
        if apple>orange:
            while len(stack) and stack[-1]=='j':
                stack.pop(-1)
            mx=max(mx,len(stack))
            stack=[]
            apple=0
            orange=0
        else:
            stack.append(i)
    while len(stack) and stack[-1]=='j':
        stack.pop(-1)
    mx=max(mx,len(stack))
    stack=[]
    apple=0
    orange=0
    return mx

pt1=0
pt2=0
apple=0
orange=0
res=0

while pt2<n:
    if s[pt2]=='j':
        apple+=1
    else:orange+=1
    if apple>orange or pt2==n-1:
        print(pt1, pt2)
        if pt2==n-1:pt2+=1
        ss=s[pt1:pt2][::-1]
        print(ss)
        res=max(res, check(ss))
        pt2+=1
        pt1=pt2
        apple=0
        orange=0
    else:
        pt2+=1

print(res)