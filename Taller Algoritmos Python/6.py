# Elaborar un algoritmo que permita encontrar el valor menor entre un grupo de datos
# y el número de veces que éste se presenta.

datos = int(input("Ingrese el valor de los datos: "));
numeros = [];
for i in range(0, datos):
    n = int(input("Ingrese el número: "));
    numeros.append(n);


min_num = min(numeros);

cant_minimos = numeros.count(min_num);

print("El valor mínimo es", min_num ,". Este se repite", cant_minimos, "veces.");