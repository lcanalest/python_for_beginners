# Exponent Function (2:41:21)


def raise_to_power(base_num, pow_num):
    result = 1

    for index in range(pow_num):
        result = result * base_num

    return result


result_pow = raise_to_power(2, 3)
print(result_pow)


# Más fácil easy papayita :V
print(2**3)