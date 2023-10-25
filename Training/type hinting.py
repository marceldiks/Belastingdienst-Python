
def print_goodmorning(name):
    print('Goodmorning %s' % name)


def telop(a: int, b: int) -> tuple[int, int]:
    return a + b, a - b


print(telop(23, 65))

name = 'Albert'
print_goodmorning(name)

