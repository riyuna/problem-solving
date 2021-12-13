n=int(input())
a=n+130
if a%100>=60:
    a+=40
a%=2400
print(f'{n} in Ottawa')
print(f'{(n-300)%2400} in Victoria')
print(f'{(n-200)%2400} in Edmonton')
print(f'{(n-100)%2400} in Winnipeg')
print(f'{n} in Toronto')
print(f'{(n+100)%2400} in Halifax')
print(f"{a} in St. John's")