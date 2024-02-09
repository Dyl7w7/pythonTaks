# Una institución educativa estableció un programa para estimular a los alumnos con buen rendimiento académico
# y que consiste en lo siguiente:
# - Si el promedio es de 9.5 o mas y el alumno es de preparatoria, entonces este podrá cursar 55 unidades y se
# le hará un 25% de descuento.
# - Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de preparatoria, entonces este podrá
# cursar 50 unidades y se le hará un 10% de descuento.
# - Si el promedio es mayor que 7 y menor que 9 y el alumno es de preparatoria, este podrá cursar 50 unidades
# y no tendrá ningún descuento.
# - Si el promedio es de 7 o menor, el numero de materias reprobadas es de 0 a 3 y el alumno es de preparatoria,
# entonces podrá cursar 45 unidades y no tendrá descuento.
# - Si el promedio es de 7 o menor, el numero de materias reprobadas es de 4 o mas y el alumno es de
# preparatoria, entonces podrá cursar 40 unidades y no tendrá ningún descuento.
# - Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y se
# le hará un 20% de descuento.
# - Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y no tendrá
# descuento.
# - Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de profesional es de $300 por
# cada cinco unidades y para alumnos de preparatoria es de $180 por cada cinco unidades.

grade = int(input("1. Preparatoria / 2. Profesional: "));
if(grade == 1):
    valorx5Uni = 180;
elif(grade == 2):
    valorx5Uni = 300;
else:
    print("Error, valor no válido");

prom = float(input("Promedio del alumno: "));
if(prom <= 7):
    subLose = int(input("Materias reprobadas: "));

if(prom >= 9.5 and grade == 1):
    print("Podrá cursar 55 unidades. 25% de descuento");
    desc = 0.25;
    maxUni = 55;
elif(prom >= 9 and prom < 9.5 and grade == 1):
    print("Prodrá cursar 50 unidades. 10% de descuento");
    desc = 0.1;
    maxUni = 50;
elif(prom > 7 and prom < 9 and  grade == 1):
    print("Podrá cursar 50 unidades. Sin descuento");
    desc = 0;
    maxUni = 50;
elif(prom <= 7 and subLose <= 3 and subLose >= 0 and grade == 1):
    print("Podrá cursar 45 unidades. Sin descuento");
    desc = 0;
    maxUni = 45;
elif(prom <= 7 and subLose >= 4 and grade == 1):
    print("Podrá cursar 40 unidades. Sin descuento");
    desc = 0;
    maxUni = 40;
elif(prom >= 9.5 and grade == 2):
    print("Podrá cursar 55 unidades. 20% de descuento");
    desc = 0.2;
    maxUni = 55;
elif(prom < 9.5 and  grade == 2):
    print("Podrá cursar 55 unidades. Sin descuento");
    desc = 0;
    maxUni = 55;
    
uniCursar = int(input("Unidades a cursar: "));
while(uniCursar > maxUni or uniCursar <= 0):
    print("Debe ingresar un número válido");
    uniCursar = int(input("Unidades a cursar: "));
    
calcUnids = uniCursar / 5;
    
subTotal = calcUnids * valorx5Uni;
total = subTotal * (1 - desc);

print("El total es de $", total)