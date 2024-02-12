# Funciones

import random as rnd

# Ingresar datos
def ingresarLista():
    lista = [];
    ndata = int(input("Ingrese la cantidad de números a agregar: "));
    for i in range(0, ndata):    
        data = int(input("Ingrese un número para la lista: "));
        lista.append(data);
        print("Se agregó", data, "a la lista");
    return lista

# Ordenar datos
def ordenarLista():
    lista1.sort();
    return lista1;

# Buscar datos
def buscarDatoLista():
    data = int(input("Ingrese el dato a buscar: "));
    if data in lista1:
        print("El número", data, "está en la lista");
    else:
        print("El número no está en la lista");
    
# Eliminar datos
def  eliminarDatoLista():
    data = int(input("Ingresé el dato a eliminar: "));
    if data in lista1:
        lista1.remove(data);
        print("Se eliminó el dato de la lista");
    else:
        print("El dato no existe en la lista");
    
# Mostrar datos
def mostrarLista():
    print(lista1);
    
# Actualizar datos
def actualizarDatoLista():
    data = int(input("Ingrese el número que desea actualizar: "));
    if data in lista1:
        dataUpdate = int(input("Ingrese el nuevo número: "));
        ind = lista1.index(data);
        lista1[ind] = dataUpdate;
        print("Se actualizó el número correctamente");

# Ingresar random
def ingresarRandom():
    lista = [];
    for i in range(20):
        lista.append(rnd.randint(1,100));
    return lista;

# Inicio del programa
lista1 = [];
select = 1;

while (select != 0):
    print("");
    print("Menu de listas");
    print("1. Ingresar datos a la lista");
    print("2. Ordenar los datos de la lista");
    print("3. Buscar un dato de la lista");
    print("4. Remover datos de la lista");
    print("5. Mostrar la lista");
    print("6. Actualizar un dato de la lista");
    print("7. Ingresar datos random a la lista");
    print("0. Salir");
    select = int(input("Seleccione la opción: "));
    print("");
    if(select == 1):
        print("La opción fue 1");
        lista1 = ingresarLista();
        print(lista1);
    elif(select == 2):
        print("La opción fue 2");
        lista1 = ordenarLista();
        print(lista1);
    elif(select == 3):
        print("La opción fue 3");
        buscarDatoLista();
    elif(select == 4):
        print("La opción fue 4");
        eliminarDatoLista();
    elif(select == 5):
        print("La opción fue 5");
        mostrarLista();
    elif(select == 6):
        print("La opción fue 6");
        actualizarDatoLista();
    elif(select == 7):
        print("La opción fue 7");
        lista1 = ingresarRandom();
    else:
        print("Opción no válida");