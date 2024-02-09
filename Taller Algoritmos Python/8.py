# En un supermercado una ama de casa pone en su carrito los artículos que va
# tomando de los estantes. La señora quiere asegurarse de que el cajero le cobre
# bien lo que ella ha comprado, por lo que cada vez que toma un artículo anota su
# precio junto con la cantidad de artículos iguales que ha tomado y determina
# cuánto dinero gastara en ese artículo; a esto le suma lo que ira gastando en los
# demás artículos, hasta que decide que ya tomo todo lo que necesitaba. Ayúdale
# a esta señora a obtener el total de sus compras.

i = 0;
subTotal = 0;

while(i == 0):
    valor = float(input("Ingrese el valor del artículo: "));
    cant = int(input("Ingrese la cantidad de artículos: "));
    articleCost =  valor * cant;
    subTotal = subTotal + articleCost;
    
    print("El subtotal es: $",subTotal);
    print("");
    print("¿Continuar?");
    i = int(input("0. Si / 1. No:  "));
    
print("El total de las compras es: $",subTotal);
    