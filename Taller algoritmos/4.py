# EL gobierno desea reforestar un bosque que mide determinado número de hectáreas. Si la superficie
# del terreno excede 1 millón de metros cuadrados, entonces decidirá sembrar de la siguiente manera:
# 70% Pinos
# 20% Oyamel
# 10% Cedro
# Si la superficie del terreno es menor o igual a 1 millón de metros cuadrados, entonces decidirá sembrar
# de la siguiente manera:
# 50% Pino
# 30% Oyamel
# 20% Cedro
# El gobierno desea saber el número de pinos, oyameles y cedros que tendrá que sembrar en el bosque, si se sabe
# que en 10 metros cuadrados caben 8 pinos, en 15 metros cuadrados caben 15 oyameles y en 18 metros cuadrados
# caben 10 cedros. También se sabe que una hectárea equivale a 10 mil metros cuadrados.

terreno = int(input("Ingrese el tamaño del terreno en hectáreas: "));
mtQ = terreno * 10000;

mtPino = 0.8;
mtOyamel = 1;
mtCedro = 0.55;

if (mtQ > 1000000):
    terrenoPinos = (mtQ * 0.7 * 0.8);
    terrenoOyamels = (mtQ * 0.2 * 1);
    terrenoCedros = (mtQ * 0.1 * 0.55);
    # terrenoPinos = ((mtQ * 0.7) / 10) * 8;
    # terrenoOyamels = ((mtQ * 0.2) / 10) * 15;
    # terrenoCedros = ((mtQ * 0.1) / 10) * 10;
elif (mtQ <= 1000000):
    terrenoPinos = (mtQ * 0.5 * 0.8);
    terrenoOyamels = (mtQ * 0.3 * 1);
    terrenoCedros = (mtQ * 0.2 * 0.55);
    # terrenoPinos = ((mtQ * 0.5) / 10) * 8;
    # terrenoOyamels = ((mtQ * 0.3) / 10) * 15;
    # terrenoCedros = ((mtQ * 0.2) / 10) * 10;
    
print("Se  plantaran", round(terrenoPinos / 8), "pinos");
print("Se  plantaran", round(terrenoOyamels / 8), "oyameles");
print("Se  plantaran", round(terrenoCedros / 8), "cedros");
    
    
