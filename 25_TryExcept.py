# Try Except (3:04:19)

## Colocando un except genérico, lo cual no es una buena práctica
try:
    num = input("Please enter a number: ")
    print(int(num))
except:
    print("Invalid input")


## Colocando except específico
print("")
try:
    num = input("Please enter a number: ")
    print(int(num))
except ValueError as err:
    # print("Invalid input")
    print(err)


## Colocando except específico para 2 posibles errores
print("")
try:
    result = 10 / 0
    num = input("Please enter a number: ")
    print(int(num))
except ValueError as err:
    # print("Invalid input")
    print(err)
except ZeroDivisionError as err:
    print(err)