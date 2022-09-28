import math

gj = print('Посчитали? Молодцы, пользуйтесь чаще!')

print("""Выберите действие:
1. Калькулятор
2. Калькулятор квадратных уравнений""")
Vibor = int(input())

if Vibor == 1:
        want = input('Какую операцию необходимо провести (+,-,/,*) ')
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if want == '+' :
                c = a + b
                print("Ответ:", c)
                print('Посчитали? Молодцы, пользуйтесь чаще!')
        elif want == '-' :
                c = a - b
                print("Ответ:", c)
                print('Посчитали? Молодцы, пользуйтесь чаще!')
        elif want == '/' :
                c = a / b
                print("Ответ:", c)
                print('Посчитали? Молодцы, пользуйтесь чаще!')
        elif want == '*':
                c = a * b
                print("Ответ:", c)
                print('Посчитали? Молодцы, пользуйтесь чаще!')


if Vibor == 2:
        print("Введите первое число")
        q = int(input())
        print("Введите второе число")
        w = int(input())
        print("Введите третье число")
        e = int(input())
        
        D = (w ** 2) - (4 * q * e)

        if D < 0:
                print("Решений нет")

        if D == 0:
                otvet = -w / (2 * q)
                s = str(otvet)
                print("Корень уравнения: ", s)

        if D > 0:
                x1 = (-w + math.sqrt(D)) / (2 * q)
                x2 = (-w - math.sqrt(D)) / (2 * q)
                s1 = str(x1)
                s2 = str(x2)
                print("Корни квадратного уравнения: ", s1, " и ", s2)