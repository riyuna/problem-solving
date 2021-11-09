while True:
    s=input()
    if s=='#':break
    res=0
    for i in s:
        res*=8
        if i=='\\':res+=1
        if i=='(':res+=2
        if i=='@':res+=3
        if i=='?':res+=4
        if i=='>':res+=5
        if i=='&':res+=6
        if i=='%':res+=7
        if i=='/':res-=1
    print(res)