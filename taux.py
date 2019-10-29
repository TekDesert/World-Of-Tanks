t = float(input("insérer vautre taux\n"))
a = 0
b = 1
while b < 2 :
    b = b*(1+t)
    a = a + 1
print(("il vous faudra " + str(a) + " années"))


type(a)