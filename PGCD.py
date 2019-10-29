b = int(input("Entrer la valeur de b \n"))
a = int(input("Entrer la valeur de a \n"))
if b > 0 or b < 0 :
    while r > 0 :
        r = a/b
        a = b
        b = r

else :
    print(" b=0 , l'opération ne peut pas être effectuée")

print(r)