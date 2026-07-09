def is_armstrong_number(number):
    num_digits = len(str(number))
    digits = [int(digit) for digit in str(number)]
    total = 0
    for digit in digits:
        total += digit ** num_digits

    if(total == number):
        return True
    return False
    pass
