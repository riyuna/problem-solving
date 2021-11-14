for i in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    A,B,C,D,E,F,G=map(int,input().split())
    gd=a+b*2+c*3+d*3+e*4+f*10
    sr=A*1+B*2+C*2+D*2+E*3+F*5+G*10
    if gd>sr:print(f"Battle {i+1}: Good triumphs over Evil")
    elif gd==sr:print(f"Battle {i+1}: No victor on this battle field")
    else:print(f"Battle {i+1}: Evil eradicates all trace of Good")