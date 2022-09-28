# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

oper = """Выбор действия:
1. +
2. -
3. *
4. /
5. Квадратное уравнение"""
print(oper)
deistvie = int(input())
if deistvie == 1:
    print("Первое число")
    x = int(input())
    print("Второе число")
    y = int(input())
    res = x + y
    stroka = str(res)
    print("Результат:", stroka)
if deistvie == 2:
    print("Первое число")
    x = int(input())
    print("Второе число")
    y = int(input())
    res = x - y
    stroka = str(res)
    print("Результат:", stroka)
if deistvie == 3:
    print("Первое число")
    x = int(input())
    print("Второе число")
    y = int(input())
    res = x * y
    stroka = str(res)
    print("Результат:", stroka)
if deistvie == 4:
    print("Первое число")
    x = int(input())
    print("Второе число")
    y = int(input())
if y == 0:
    print("Разделить на ноль нельзя")
if y > 0:
    res = x / y
    stroka = str(res)
    print("Результат:", stroka)
if deistvie == 5:
    print("Первое число")
    a = int(input())
    print("Второе число")
    b = int(input())
    print("Третье число")
    c = int(input())
    D = (b ** 2) - (4 * a * c)
    if D < 0:
        print("Корней нет")
    if D == 0:
        res = -c / (2 * a)
        stroka = str(res)
        print("Дискриминант:", stroka)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        stroka1 = str(x1)
        stroka2 = str(x2)
        print("Корни квадратного уравнения:", stroka1, ";",stroka2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
