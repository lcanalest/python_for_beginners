num1 = float(input("Ingrese el primer número: "))
operacion = input("Ingrese la operación matemática a realizar: ")
num2 = float(input("Ingrese el segundo número: "))

# Suma, Resta, Multiplicación, División
if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    print(num1 / num2)