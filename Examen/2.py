op = 0
while (op == 0):
    totalPagar = 0
    montoAdicional = 0
    kmExceso = 0
    totalMonto = 0
    montoFijo = 300000
    km = int(input("Ingrese los kilómetros recorridos: "))
    if(km > 500 and km <= 1000):
        kmExceso = km - 500
        montoAdicional = 15000
        totalMonto = kmExceso * montoAdicional
        totalPagar = totalMonto + montoFijo
        iva = totalPagar * 0.2
    elif(km > 1000):
        kmExceso = km - 1000
        totalMontox500 = 500 * 15000
        montoAdicional = 10000
        totalMonto = kmExceso * montoAdicional + totalMontox500
        totalPagar = totalMonto + montoFijo
        iva = totalPagar * 0.2
    else:
        totalPagar = montoFijo
        iva = totalPagar * 0.2

    print("El monto adicional por exceso de kilómetros es: $",totalMonto)
    print("El total a pagar es: $",totalPagar)
    print("El impuesto equivale a: $",iva)
    print()
    print("###########################################################")
    print("¿Desea continuar? \n 0. Si  /  1. No")
    op = int(input())