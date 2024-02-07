# Condicionales

n1 = int(input("Ingrese el primer número: "));
n2 = int(input("Ingrese el segundo número: "));

if (n2 > n1):
    total = n1 + n2;
elif (n1 > n2):
    total = n1 - n2;
elif (n1 == n2):
    total = n1 * n2;
else:
    total = n1 / n2;
    
print ("El resultado de la operación es: " + str(total));