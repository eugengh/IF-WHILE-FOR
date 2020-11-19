a=eval(input("Introdu a "))
b=eval(input("Introdu b "))
c=eval(input("Introdu c "))
if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    if (a==b)and(a==c)and(b==c):
        print("Da, echilateral")
    elif (a==b)and(a!=c)and(b!=c):
        print("Da, isoscel")
    else:
        print("Da, Scalen")
else:
    print("error")