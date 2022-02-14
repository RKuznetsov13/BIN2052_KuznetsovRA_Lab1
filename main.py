
from math import sqrt

# Решаем над полем действительных чисел
print('Введите коэффициенты квадратного уранения вида ax^2+bx+c:')

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

discriminant = b ** 2 - 4 * a * c
print('D = {}'.format(discriminant))

if discriminant >= 0:
    x1 = -b + sqrt(discriminant) / (2 * a)
    x2 = -b - sqrt(discriminant) / (2 * a)
    if x1 != x2:
        print('Корень х1 = {x1}\nКорень х2 = {x2}'.format(x1=x1, x2=x2))
    else:
        print('Корень х0 = {}'.format(x1))
else:
    print('В действительном поле корней нет')