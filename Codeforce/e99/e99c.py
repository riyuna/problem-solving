for i in ' '*(int(input())):
    x,y=map(int,input().split())
    if y==0:print(x, y)
    else:
        if x==0:print(x,y)
        else:print(x-1, y)