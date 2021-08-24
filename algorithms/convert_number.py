DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(representation, source_base, target_base):
    if representation == '0':
        return '0'
    representation = representation.upper()
    return to_base(from_base(representation, source_base), target_base)

def from_base(representation, source_base):
    total = 0
    for i, v in enumerate(representation[::-1]):
        total += digit_to_int(v) * source_base ** i
    return total

def to_base(integer, target_base):
    representation = ''
    while integer:
        integer, remainder = divmod(integer, target_base)
        representation += int_to_digit(remainder)
    return representation[::-1]

def digit_to_int(digit):
    return DIGITS.index(digit)

def int_to_digit(integer):
    return DIGITS[integer]