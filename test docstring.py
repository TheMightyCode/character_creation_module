from math import sqrt

print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа')


def calculatesquareroot(number: int) -> int:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: int) -> bool:
    if your_number <= 0:
        return

    print(f"Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {calculatesquareroot(your_number)}")


calc(25.5)
