import math
n=eval(input("Introdu n "))
m=eval(input("Introdu m "))
s=math.log(n, m)
p=round(s)
if(m**p)==n:
    print("Numarul",n, " este o putere a lui", m)
else:
    print("Numarul",n, " nu este o putere a lui", m)