# Building a Better Calculator (2:00:37)
def kani_calcualator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Operador incorrecto"


resultado = kani_calcualator(43, "/", 3)
print(resultado)
