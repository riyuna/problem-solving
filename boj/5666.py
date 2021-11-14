while True:
    try:
        a,b=map(int,input().split())
        print("{:.2f}".format(a/b))
    except:
        break