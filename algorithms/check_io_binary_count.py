#
# https://py.checkio.org/mission/binary-count/solve/

def checkio(number):
    return len("".join(filter(lambda b: b == "1", "{0:b}".format(number))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    assert checkio(0) == 0