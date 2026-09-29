def convert_binary_to_decimal(sensor_list):
    """
    Takes a list of 6 boolean/integer sensor states (ordered from sensor_0 to sensor_5),
    reverses them to preserve positional significance, and computes the decimal total.
    """
    # Reverse the list order so sensor_0 acts as the lowest-order bit (2^0)
    reversed_sensors = sensor_list[::-1]
    decimal_sum = 0

    try:
        for index, value in enumerate(reversed_sensors):
            bit = int(value)

            if bit not in (0, 1):

                return None

            power = int(index)
            decimal_sum += (bit * (2 ** power))

        return decimal_sum

    except ValueError:
        print('Error: Non-numeric data passed to converter')
        return None
