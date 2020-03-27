def long(value):
    import time
    time.sleep(5) # delays for 5 seconds

    return 'long' + str(value)


def short(string_param):
    print('Speed!', string_param)
    return 'short'


def medium(value, *modificators):
    result = value
    for m in modificators:
        result *= m

    return result


def change_sign(num, check_sign=True):
    if check_sign and num > 0:
        raise ValueError('num > 0!')
    return -num