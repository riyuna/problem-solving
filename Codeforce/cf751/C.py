def ispal(s):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:return False
    return True

def checkpal(s, t):
    pt1=0
    pt2=len(s)-1
    ct=0
    while pt1<pt2:
        if s[pt1]==s[pt2]:
            pt1+=1
            pt2-=1
            continue
        if s[pt1]==t:
            pt1+=1
            ct+=1
        elif s[pt2]==t:
            pt2-=1
            ct+=1
        else:return -1
    return ct
for _ in ' '*int(input()):
    n=int(input())
    s=input()
    L=[False]*26
    for i in s:
        L[ord(i)-97]=True
    if ispal(s):
        print(0)
        continue
    ct=-1
    for i in range(26):
        if not L[i]:continue
        t=chr(i+97)
        k=checkpal(s, t)
        if k==-1:continue
        if ct==-1:ct=k
        else:ct=min(ct,k)
    else:print(ct)