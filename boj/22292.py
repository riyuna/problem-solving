def side(x, y, z):
    if max([x,y,z])==100:return True
    return False

def P3(x, y, z):
    sideOn = side(x, y, z)
    if sideOn:return ((x-100)**2+(y-100)**2+(z-100)**2)**0.5
    else:
        a,b,c=sorted([x,y,z])
        return min((200-b)**2+(100-c)**2, (100-b)**2+(200-c)**2)**0.5
############### SUBMIT THE CODE ABOVE ONLY ###############

print(P3(0, 100, 20)) # 128.06