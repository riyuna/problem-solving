s=input().split()
n=int(input())
L=[]
for i in ' '*n:L.append(input())
team1=[]
team2=[]
curr=1
visited=[False]*n
pt=-1
for i in range(n):
	for j in range(len(s)):
		pt+=1
		pt%=n
		while visited[pt]:
			pt+=1
			pt%=n
	if curr==1:
		team1.append(L[pt])
		curr=2
	else:
		team2.append(L[pt])
		curr=1
	visited[pt]=True

print(len(team1))
for i in team1:print(i)
print(len(team2))
for i in team2:print(i)