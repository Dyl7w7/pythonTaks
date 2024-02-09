# Que lea tres números diferentes y determine el numero medio del conjunto de los tres números (el numero
# medio es aquel numero que no es ni mayor, ni menor)

num1 = int(input("Ingrese el primer número: "));
num2 = int(input("Ingrese el segundo número: "));
num3 = int(input("Ingrese el tercer número: "));

if(num1 > num2 and num2 > num3 and num1 > num3):
    print("El número medio es ", num2);
elif(num1 < num2 and num2 < num3 and num1 < num3):
    print("El número medio es ", num2);
elif(num1 < num2 and num2 > num3 and num1 > num3):
    print("El número medio es ", num1);
elif(num1 < num2 and num2 > num3 and num1 < num3):
    print("El número medio es ", num3);
elif(num1 > num2 and num2 < num3 and num1 < num3):
    print("El número medio es ", num1);
elif(num1 > num2 and num2 < num3 and num1 > num3):
    print("El número medio es ", num3);