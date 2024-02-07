# Una frutería ofrece las manzanas con descuento según la siguiente tabla:
# NUM. DE KILOS COMPRADOS % DESCUENTO
#   0 - 2 0%
#   2.01 - 5 10%
#   5.01 - 10 15%
#   10.01 en adelante 20%
# Determinar cuánto pagara una persona que compre manzanas es esa frutería.

i = 0;
while (i == 0):
    numKilos = int(input("Ingrese los kilos a comprar: "));
    applePrice = 10000;
    if(numKilos <= 2 and numKilos >= 0):
        totalPrice = applePrice * numKilos;
        print("Descuento del 0%");
        print("Total a pagar: ", totalPrice);
    elif(numKilos <= 5 and numKilos > 2):
        desc = 0.1;
        totalSinDesc = applePrice * numKilos;
        totalDesc = totalSinDesc * (1 - desc);
        print("Descuento del 10%");
        print("Total a pagar: ", totalDesc);
    elif(numKilos <= 10 and numKilos > 5):
        desc = 0.15;
        totalSinDesc = applePrice * numKilos;
        totalDesc = totalSinDesc * (1 - desc);
        print("Descuento del 15%");
        print("Total a pagar: ", totalDesc);
    elif(numKilos > 10):
        desc = 0.2;
        totalSinDesc = applePrice * numKilos;
        totalDesc = totalSinDesc * (1 - desc);    
        print("Descuento del 20%");
        print("Total a pagar: ", totalDesc);
    else:
        print("Error, valor no válido");
        
    print("¿Desea continuar?");
    i = int(input("0. Si / 1. No:  "));
    while (i != 0 and i != 1):
        print("Error, opción no válida");
        i = int(input("0. Si / 1. No:  "));