from turtle import pos


n=int(input())
pre_check=[-1]*(300001)
pos_check=[-1]*(300001)
pre_list=[[]for i in range(n)] #0번째부터 i번째까지로 만들 수 있는 수
pos_list=[[]for i in range(n)] #i번째부터 n-1번째까지로 만들 수 있는 수
#pre
pre_check[0]=0
for i in range(n):
	