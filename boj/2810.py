n=int(input())
s=input()
ct=s.count('L')
print(min(n+1-ct//2, n))