# Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un medico determina
# si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de
# su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se
# determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el medico se basa
# para obtener el resultado es la siguiente:

# EDAD NIVEL HEMOGLOBINA
# 0 - 1 mes 13 - 26 g%
# > 1 y < = 6 meses 10 - 18 g%
# > 6 y < = 12 meses 11 - 15 g%
# > 1 y < = 5 años 11.5 - 15 g%
# > 5 y < = 10 años 12.6 - 15.5 g%
# > 10 y < = 15 años 13 - 15.5 g%
# mujeres > 15 años 12 - 16 g%
# hombres > 15 años 14 - 18 g%

print("¿Desea ingresar su edad en meses o en años?");
opcion = 0;
while(opcion != 1 and opcion != 2):
    opcion = int(input("1. Años / 2. Meses: "));
    if(opcion != 1 and opcion != 2):
        print("Opción incorrecta");
if(opcion == 1):
    edad = int(input("Ingrese su edad en años: "));
elif(opcion == 2):
    edadMeses = int(input("Ingrese su edad en meses: "));
else:
    print("Opción incorrecta");

if(edad > 15):
    print("Ingrese su genero");
    genero = int(input("1. Mujer / 2. Hombre"));
    while(genero != 1 and genero != 2):
        print("Error, opción no válida");
        genero = int(input("1. Mujer / 2. Hombre"));
hmg = float(input("Ingrese su porcentaje (%) de hemoglobina: "));

if(edadMeses > 0 and edadMeses <= 1):
    if(hmg >= 13 and hmg <= 26):
        print("Anemia: Negativo");
    elif(hmg > 26):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edadMeses > 1 and edadMeses <= 6):
    if(hmg >= 10 and hmg <= 18):
        print("Anemia: Negativo");
    elif(hmg > 18):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edadMeses > 6 and edadMeses <= 12):
    if(hmg >= 11 and hmg <= 15):
        print("Anemia: Negativo");
    elif(hmg > 15):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edad > 1 and edad <= 5):
    if(hmg >= 11.5 and hmg <= 15):
        print("Anemia: Negativo");
    elif(hmg > 15):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edad > 5 and edad <= 10):
    if(hmg >= 12.6 and hmg <= 15.5):
        print("Anemia: Negativo");
    elif(hmg > 15.5):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edad > 10 and edad <= 15):
    if(hmg >= 13 and hmg <= 15.5):
        print("Anemia: Negativo");
    elif(hmg > 15.5):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edad > 15 and genero == 1):
    if(hmg >= 12 and hmg <= 16):
        print("Anemia: Negativo");
    elif(hmg > 16):
        print("Anemia: Negativo");
    else:
        print("Anemia: Positivo");
elif(edad > 15 and genero == 2):
    if(hmg >= 14 and hmg <= 18):
        print("Anemia: Negativo");
    elif(hmg > 18):
        print("Anemia: Negativo");
    else:
        print("Anemia Positivo");