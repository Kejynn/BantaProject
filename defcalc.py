import math

print("""Выберите действие:
1. Калькулятор
2. Калькулятор квадратных уравнений""")
Vibor = int(input())

if Vibor == 1:
    want = input('Какую операцию необходимо провести (+,-,/,*) ')
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if want == '+':
        def sum(a, b):
            return a + b
        print("Ответ:" )
        print(str(a + b))
        print('Посчитали? Молодцы, пользуйтесь чаще!')

    elif want == '-':
        def raz(a, b):
            return a - b
        print("Ответ:")
        print(str(a - b))
        print('Посчитали? Молодцы, пользуйтесь чаще!')

    elif want == '/':
        def chast(a, b):
            return a / b
        print("Ответ:")
        print(str(a / b))
        print('Посчитали? Молодцы, пользуйтесь чаще!')

    elif want == '*':
        def pr(a, b):
            return a * b
        print("Ответ:")
        print(str(a * b))
        print('Посчитали? Молодцы, пользуйтесь чаще!')

if Vibor == 2:
    print("Введите первое число")
    q = int(input())
    print("Введите второе число")
    w = int(input())
    print("Введите третье число")
    e = int(input())
    D = (w ** 2) - (4 * q * e)

    def disc(q, w, e):
        return (w ** 2) - (4 * q * e)

    otvet = -w / (2 * q)
    s = str(otvet)
    print("Корень уравнения: ", s)


    def disc0(q, w):
        return -w / (2 * q)
    print("Корней нет")


    def koren(q, w, D):
        return (-w + math.sqrt(D)) / (2 * q), (-w - math.sqrt(D)) / (2 * q)




