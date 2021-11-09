while True:
    a,b,c=input().split()
    if a==c=='0' and b=='W':break
    if b=='W':
        k=int(a)-int(c)
    if b=='D':
        k=int(a)+int(c)
    if k<-200:print('Not allowed')
    else:print(k)