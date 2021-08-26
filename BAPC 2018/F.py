n, retire = map(int,input().split())

item = []

for i in range(n):
    item.append(list(map(int,input().split())))

start = 1
end = 4*10**9

def check(k):
    res=0
    for i in range(n):
        indv = item[i][0]*k-item[i][1]
        if indv>=0:res+=indv
    return res
for i in range(40):
    k = (start+end)//2
    invest = check(k)
    if invest >= retire:
        end = k
    else:
        start = k
candidate = [end-1, end, end+1]
for i in candidate:
    if check(i)>=retire:
        print(i)
        break