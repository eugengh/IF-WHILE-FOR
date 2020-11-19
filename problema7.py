n=eval(input("Cati ani are Mihai? "))
p=1
bani=0
if n<20:
    for x in range(1, n+1):
        p=p*2
        bani+=p+x
    print("Mihai a primit {} bani, cand avea {} ani".format(bani, n))
else:
    print("Trebuie sa introduci un numar mai mic ca 20")
print("La 6 ani el va avea mai mult de 100$")