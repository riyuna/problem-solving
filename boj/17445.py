L=input().split(',')
if len(L)==2:L[1]=L[1][:(len(L[1]))-1]
a,b,c=int(L[0][6:]) if len(L)>1 else 0, int(L[1]) if len(L)>1 else int(L[0][6:len(L[0])-1]), int(L[2][:len(L[2])-1]) if len(L)>2 else 1

def check(n):
    if n==1:return True
    while n>1:
        if n%10:return False
        n//=10
    return True

l=(b-a+c-1)//c if c>0 else (a-b+abs(c)-1)//(abs(c))

if l<0:l=0

if l==0:
    print('range(-1)')

if l==1:
    start=a
    if start==-1:print('range(-1,-10,-10)')
    elif start==-2:print('range(-2,-1)')
    else:
        if -1<start:
            c=-1
            while start+c>-1:
                c*=10
        else:
            c=1
            while start+c<-1:
                c*=10
        print(f'range({start},-1,{c})')

if l>1:
    start=a
    diff=c
    end=start+diff*(l-1)
    if c>0:
        s,e=end+1, end+diff
    else:
        s,e=end+diff, end-1
    if s<=-1<=e:
        mid=-1
    else:
        if len(str(s))==len(str(e)):
            if abs(s)<abs(e):mid=s
            else:mid=e
        else:
            k=min(len(str(s)),len(str(e)))
            flag=s//abs(s)
            if flag==-1:k-=1
            mid=flag
            while mid<s or mid>e:
                mid*=10
            if s==0:mid=0
    print(f'range({start},{mid},{diff})') if diff!=1 else print(f'range({start},{mid})')