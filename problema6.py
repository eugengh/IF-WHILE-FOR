n=eval(input("n= "))
s1=0
for x in range(1, n+1, 1):
    s1=s1+(x**3)
print(s1)

s2=0
for x in range(1, n+1, 1):
    s2+=x
    s2=s2**2
print(s2)
if s1>s2:
    print("S1 mai mare ca S2")
elif s1<s2:
    print("S1 mai mic ca S2")
else:
    print("S1=S2")


