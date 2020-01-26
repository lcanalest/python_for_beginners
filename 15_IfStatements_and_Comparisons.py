# If Statements and Comparisons (1:54:09)


def max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = max_number(42, 31, 11)
print(result)