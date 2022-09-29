import math

Zadanie = """Выберите действие:
1. Сложение 
2. Умножение
3. Деление 
4. Вычитание 
5. Квадратное уравнение"""
print(Zadanie)
vibrannoe_deystvie = int(input())
if vibrannoe_deystvie == 1:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    Result = x + y
    stroka = str(Result)
    print("Ответ: ", stroka)
if vibrannoe_deystvie == 2:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    Result = x * y
    stroka = str(Result)
    print("Ответ: ", stroka)
if vibrannoe_deystvie == 3:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    if y == 0:
        print("На ноль делить нельзя")
    else:
        Result = x / y
        stroka = str(Result)
        print("Ответ: ", stroka)
if vibrannoe_deystvie == 4:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    Result = x - y
    stroka = str(Result)
    print("Ответ: ", stroka)
if vibrannoe_deystvie == 5:
    print("Введите первое число")
    x = int(input())
    print("Введите второе число")
    y = int(input())
    print("Введите третье число")
    z = int(input())
    disc = (y ** 2) - (4 * x * z)
    if disc < 0:
        print("Корней нет")
    if disc == 0:
        Result = -y / (2 * x)
        stroka = str(Result)
        print("Корень уравнения: ", stroka)
    if disc > 0:
        koren1 = (-y + math.sqrt(disc)) / (2 * x)
        koren2 = (-y - math.sqrt(disc)) / (2 * x)
        stroka1 = str(koren1)
        stroka2 = str(koren2)
        print("Корни квадратного уравнения: ", stroka1, " и ", stroka2)
if vibrannoe_deystvie < 1 or vibrannoe_deystvie > 5:
    print("Ошибка: введите число от 1 до 5")
