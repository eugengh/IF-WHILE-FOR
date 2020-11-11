#PROBLEMA 1
n=eval(input("n="))
if n in (28, 29, 30, 31):
    if n==28:
        print("Februarie")
    elif n==29:
        print("Februarie, an bisect")
    elif n==30:
        print("aprilie, iunie, septembrie, noiembrie")
    elif n==31:
        print("ianuarie, martie, mai, iulie, august, octombrie, decembrie")
else:
    print("Trebuie sa introduci num 29 ori 29 ori 30 ori 31")
#PROBLEMA 2
p=1
s=0
n=eval(input("n="))
if n>1:
    for x in range(1, n+1):
        p=p*x
        s=s+p
    print("s=", s)
else:
    print("n trebuie sa fie mai mare ca 1")
