# En un supermercado un cajero captura los precios de los artículos que los
# clientes compran e indica a cada cliente cual es el monto de lo que deben
# pagar. Al final del día le indica a su supervisor cuanto fue lo que cobro en total a
# todos los clientes que pasaron por su caja.

i = 0;
total = 0;
while(i == 0):
    articleCost = float(input("Ingrese el total: "));
    total = total + articleCost;
    print("Total a pagar: $",articleCost);
    print("¿Final del día?");
    i = int(input("1. Si / 0. No"));
    
print("Cobro total del día: $",total);