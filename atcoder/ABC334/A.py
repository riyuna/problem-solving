import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
#print('なんでや!阪神関係ないやろ!')

b,g=linput()
print("Bat"if b>g else "Glove")