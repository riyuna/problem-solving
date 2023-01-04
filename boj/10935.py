import base64
s=input().strip().encode('ascii')
s=base64.b64encode(s)
s=s.decode('ascii')
print(s)