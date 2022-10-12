

import math

oper = """Выбор действия:
1. +
2. -
3. *
4. /
5. Квадратное уравнение"""
print(oper)
deistvie = int(input())
if 0 < deistvie < 5:
    x = int(input("Введите первое число"))
    y = int(input("Введите второе число"))
    def plus(a, b):
        return a + b
    def minus(a, b):
        return a - b
    def delenie(a, b):
        return a / b
    def umnogenie(a, b):
        return a * b

    if deistvie == 1:
        print("Результат:", plus(x, y))

    elif deistvie == 2:
        print("Результат:", minus(x, y))

    elif deistvie == 3:
        if y == 0:
            print("На ноль делить нельзя")
        else:
            print("Результат:", delenie(x, y))

    elif deistvie == 4:
        print("Результат:", umnogenie(x, y))

elif deistvie == 5:
    a = int(input("Введите первое число"))
    b = int(input("Введите второе число"))
    c = int(input("Введите третье число"))
    def D (x, y, z):
        return (y ** 2) - (4 * x * z)
    def D0(x, y):
        return  -y / (2 * x)
    def koren(x, y, disk):
        return(-y + math.sqrt(disk)) / (2 * x), (-y - math.sqrt(disk)) / (2 * x)
    disk = D(a, b, c)
    if disk < 0:
        print("Корней нет")
    if disk == 0:
        print("Корни:", D0(a, b))
    if disk > 0:
        print("Корни:", koren(a, b, disk))
else:
    print("Выбрано неверное действие. Выберите цифру от 1 до 5")

