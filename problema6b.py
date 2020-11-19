n=eval(input("n= "))
d=0
s1=1
b=0
for x in range(1, n+1, 1):
    d=d+(x**2)
    s1=d*3
print(s1)
s2=0
for x in range(1,n+1,1):
    b+=x
    s2=b+(n**3)+(n**2)
print(s2)
if s1>s2:
    print("S1 mai mare ca S2")
elif s1<s2:
    print("S1 mai mic ca S2")
else:
    print("S1=S2")


